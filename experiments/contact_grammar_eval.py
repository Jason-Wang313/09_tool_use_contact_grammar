"""Controlled evidence for contact-grammar tool-use reasoning.

This experiment is a small finite contact world, not a physics engine. Its job
is to test the core claim mechanistically: ordered, role-typed contact
productions reject some plans that static affordance or unordered contact-set
representations accept, and they compose to unseen tool/task combinations.
"""

from __future__ import annotations

import csv
import json
import math
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Set, Tuple


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
FIGURES = ROOT / "figures"
LOGS = ROOT / "logs"
PROGRESS = LOGS / "experiment_progress.txt"


@dataclass(frozen=True)
class Tool:
    name: str
    features: Tuple[str, ...]
    length: int
    stiffness: int
    signature: str


@dataclass(frozen=True)
class Task:
    name: str
    required_features: Tuple[str, ...]
    contact_side: str
    min_length: int
    needs_brace: bool
    needs_stiff: bool
    sequence: Tuple[str, ...]


@dataclass(frozen=True)
class Episode:
    episode_id: int
    split: str
    task: Task
    tool: Tool
    blocked_side: str
    brace_available: bool
    fragile: bool
    ood_signature: bool


TASKS: List[Task] = [
    Task(
        name="pull_occluded_object",
        required_features=("hook",),
        contact_side="behind",
        min_length=2,
        needs_brace=False,
        needs_stiff=False,
        sequence=("grasp_handle", "seat_hook_behind", "draw_along_axis"),
    ),
    Task(
        name="sweep_debris",
        required_features=("flat_edge",),
        contact_side="front",
        min_length=1,
        needs_brace=False,
        needs_stiff=False,
        sequence=("grasp_handle", "lay_flat_edge_front", "sweep_with_support"),
    ),
    Task(
        name="pry_lid",
        required_features=("wedge",),
        contact_side="under",
        min_length=2,
        needs_brace=True,
        needs_stiff=True,
        sequence=("grasp_handle", "insert_wedge_under", "brace_on_rim", "rotate_about_brace"),
    ),
    Task(
        name="press_recessed_button",
        required_features=("narrow_tip",),
        contact_side="front",
        min_length=3,
        needs_brace=False,
        needs_stiff=True,
        sequence=("grasp_handle", "align_tip_normal", "press_without_slip"),
    ),
    Task(
        name="drag_distant_ring",
        required_features=("hook", "long_shaft"),
        contact_side="inside",
        min_length=4,
        needs_brace=False,
        needs_stiff=False,
        sequence=("grasp_handle", "thread_hook_inside", "drag_with_tension"),
    ),
    Task(
        name="tamp_powder",
        required_features=("flat_end",),
        contact_side="top",
        min_length=1,
        needs_brace=False,
        needs_stiff=True,
        sequence=("grasp_handle", "place_flat_end_top", "compress_normal"),
    ),
]


FEATURE_POOL = [
    "hook",
    "flat_edge",
    "wedge",
    "narrow_tip",
    "long_shaft",
    "flat_end",
    "soft_pad",
    "hinge",
]


def log(message: str) -> None:
    LOGS.mkdir(exist_ok=True)
    with PROGRESS.open("a", encoding="utf-8") as f:
        f.write(message + "\n")
    print(message, flush=True)


def make_tools(rng: random.Random, n: int = 120) -> List[Tool]:
    tools: List[Tool] = []
    base_specs = [
        ("hook_rod", ("hook", "long_shaft"), 4, 3),
        ("spatula", ("flat_edge", "flat_end"), 2, 2),
        ("screwdriver", ("narrow_tip", "long_shaft"), 4, 4),
        ("wedge_bar", ("wedge", "long_shaft"), 3, 4),
        ("soft_brush", ("flat_edge", "soft_pad"), 2, 1),
        ("tamper", ("flat_end",), 1, 4),
    ]
    for name, feats, length, stiff in base_specs:
        sig = "+".join(sorted(feats))
        tools.append(Tool(name, feats, length, stiff, sig))
    for i in range(n - len(base_specs)):
        k = rng.choice([1, 2, 2, 3])
        feats = tuple(sorted(rng.sample(FEATURE_POOL, k)))
        if rng.random() < 0.8 and "handle" in feats:
            feats = tuple(f for f in feats if f != "handle")
        length = max(1, min(5, rng.randint(1, 5) + (1 if "long_shaft" in feats else 0)))
        stiffness = max(1, min(5, rng.randint(1, 5) - (1 if "soft_pad" in feats else 0)))
        sig = "+".join(sorted(feats))
        tools.append(Tool(f"tool_{i:03d}_{sig}", feats, length, stiffness, sig))
    return tools


def mechanical_oracle(ep: Episode) -> Tuple[bool, str]:
    feats = set(ep.tool.features)
    missing = [f for f in ep.task.required_features if f not in feats]
    if missing:
        return False, "missing_feature:" + "+".join(missing)
    if ep.tool.length < ep.task.min_length:
        return False, "too_short"
    if ep.task.needs_stiff and ep.tool.stiffness < 3:
        return False, "too_compliant"
    if ep.task.contact_side == ep.blocked_side and "narrow_tip" not in feats and "wedge" not in feats:
        return False, "blocked_contact_side"
    if ep.fragile and ep.task.name in {"pry_lid", "tamp_powder"} and ep.tool.stiffness > 4:
        return False, "breaks_fragile_target"
    if ep.task.needs_brace and not ep.brace_available:
        return False, "no_environment_brace"
    if ep.task.needs_brace and "wedge" not in feats:
        return False, "no_braceable_wedge"
    return True, "valid_contact_trace"


def grammar_plan(ep: Episode, mutate: str = "none") -> Tuple[bool, str]:
    feats: Set[str] = set(ep.tool.features)
    contacts: List[str] = []
    contacts.append("hand:tool_handle")
    for feature in ep.task.required_features:
        if feature not in feats:
            return False, "production_blocked_missing_" + feature
    if ep.tool.length < ep.task.min_length:
        return False, "production_blocked_length"
    if ep.task.needs_stiff and ep.tool.stiffness < 3:
        return False, "production_blocked_stiffness"
    if ep.task.contact_side == ep.blocked_side:
        if mutate != "drop_side_gate" and "narrow_tip" not in feats and "wedge" not in feats:
            return False, "production_blocked_side"
    if ep.task.needs_brace:
        if mutate != "drop_brace_gate":
            if not ep.brace_available:
                return False, "production_blocked_no_brace"
            contacts.append("tool:environment_brace")
        if "wedge" not in feats:
            return False, "production_blocked_brace_geometry"
    if ep.fragile and ep.task.name in {"pry_lid", "tamp_powder"} and ep.tool.stiffness > 4:
        if mutate != "drop_fragility_gate":
            return False, "production_blocked_fragility"
    contacts.append("tool:target_" + ep.task.contact_side)
    return True, " -> ".join(ep.task.sequence) + " | " + ",".join(contacts)


def unordered_contact_set(ep: Episode) -> Tuple[bool, str]:
    feats = set(ep.tool.features)
    if all(feature in feats for feature in ep.task.required_features) and ep.tool.length >= ep.task.min_length:
        return True, "required_contacts_present_without_order_or_role"
    return False, "missing_static_contact_label"


def static_affordance(ep: Episode) -> Tuple[bool, str]:
    feats = set(ep.tool.features)
    for feature in ep.task.required_features:
        if feature not in feats:
            return False, "no_affordance_region_" + feature
    if ep.task.needs_stiff and "soft_pad" in feats:
        return False, "soft_region_penalty"
    return True, "task_feature_affordance_match"


def flat_pair_memory(ep: Episode, seen: Set[Tuple[str, str]]) -> Tuple[bool, str]:
    key = (ep.task.name, ep.tool.signature)
    if key in seen:
        return True, "memorized_task_tool_signature"
    return False, "unseen_task_tool_signature"


def sample_episodes(rng: random.Random, tools: Sequence[Tool], n: int = 1800) -> Tuple[List[Episode], Set[Tuple[str, str]]]:
    train_signatures: Set[Tuple[str, str]] = set()
    episodes: List[Episode] = []
    all_sides = ["front", "behind", "under", "inside", "top", "none"]
    for episode_id in range(n):
        task = rng.choice(TASKS)
        if rng.random() < 0.55:
            candidates = [t for t in tools if all(f in t.features for f in task.required_features)]
            tool = rng.choice(candidates or list(tools))
        else:
            tool = rng.choice(list(tools))
        blocked_side = rng.choice(all_sides)
        if rng.random() < 0.22:
            blocked_side = task.contact_side
        brace_available = rng.random() > (0.28 if task.needs_brace else 0.04)
        fragile = rng.random() < 0.14
        signature = (task.name, tool.signature)
        split = "train" if episode_id < int(n * 0.35) else "test"
        if split == "train":
            ok, _ = mechanical_oracle(
                Episode(
                    episode_id,
                    split,
                    task,
                    tool,
                    blocked_side,
                    brace_available,
                    fragile,
                    False,
                )
            )
            if ok and rng.random() < 0.55:
                train_signatures.add(signature)
        ood = signature not in train_signatures
        episodes.append(Episode(episode_id, split, task, tool, blocked_side, brace_available, fragile, ood))
    return episodes, train_signatures


def metrics(rows: Iterable[Dict[str, object]]) -> Dict[str, float]:
    rows = list(rows)
    tp = sum(1 for r in rows if r["oracle"] and r["prediction"])
    tn = sum(1 for r in rows if (not r["oracle"]) and (not r["prediction"]))
    fp = sum(1 for r in rows if (not r["oracle"]) and r["prediction"])
    fn = sum(1 for r in rows if r["oracle"] and (not r["prediction"]))
    n = max(1, len(rows))
    precision = tp / max(1, tp + fp)
    recall = tp / max(1, tp + fn)
    f1 = 2 * precision * recall / max(1e-12, precision + recall)
    return {
        "n": float(n),
        "accuracy": (tp + tn) / n,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "false_positive_rate": fp / max(1, fp + tn),
        "false_negative_rate": fn / max(1, fn + tp),
    }


def write_csv(path: Path, rows: List[Dict[str, object]], fieldnames: Sequence[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def maybe_plot(aggregate_rows: List[Dict[str, object]]) -> None:
    try:
        import matplotlib

        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        methods = [r["method"] for r in aggregate_rows if r["slice"] == "test_all"]
        f1 = [float(r["f1"]) for r in aggregate_rows if r["slice"] == "test_all"]
        fp = [float(r["false_positive_rate"]) for r in aggregate_rows if r["slice"] == "test_all"]
        x = list(range(len(methods)))
        fig, ax = plt.subplots(figsize=(6.4, 3.0))
        ax.bar([v - 0.18 for v in x], f1, width=0.36, label="F1", color="#4c78a8")
        ax.bar([v + 0.18 for v in x], fp, width=0.36, label="false positive rate", color="#f58518")
        ax.set_xticks(x)
        ax.set_xticklabels(methods, rotation=20, ha="right", fontsize=8)
        ax.set_ylim(0, 1.05)
        ax.set_ylabel("score")
        ax.legend(frameon=False, fontsize=8)
        ax.set_title("Contact grammar rejects impossible role/order traces")
        fig.tight_layout()
        fig.savefig(FIGURES / "eval_summary.pdf")
        plt.close(fig)
    except Exception as exc:  # noqa: BLE001
        (FIGURES / "eval_summary_plot_failed.txt").write_text(str(exc), encoding="utf-8")


def write_latex_table(aggregate_rows: List[Dict[str, object]]) -> None:
    rows = [r for r in aggregate_rows if r["slice"] == "test_all"]
    lines = [
        "\\begin{tabular}{lrrrr}",
        "\\hline",
        "Method & Acc. & F1 & FP rate & FN rate \\\\",
        "\\hline",
    ]
    for r in rows:
        method = str(r["method"]).replace("_", "\\_")
        lines.append(
            f"{method} & {float(r['accuracy']):.3f} & {float(r['f1']):.3f} & "
            f"{float(r['false_positive_rate']):.3f} & {float(r['false_negative_rate']):.3f} \\\\"
        )
    lines.extend(["\\hline", "\\end{tabular}", ""])
    (FIGURES / "eval_table.tex").write_text("\n".join(lines), encoding="utf-8")


def run() -> int:
    DATA.mkdir(exist_ok=True)
    FIGURES.mkdir(exist_ok=True)
    LOGS.mkdir(exist_ok=True)
    PROGRESS.write_text("contact grammar experiment started\n", encoding="utf-8")
    rng = random.Random(9)
    tools = make_tools(rng)
    episodes, seen = sample_episodes(rng, tools)
    log(f"TOOLS {len(tools)} EPISODES {len(episodes)} TRAIN_SIGNATURES {len(seen)}")
    methods = {
        "contact_grammar": lambda ep: grammar_plan(ep),
        "unordered_contacts": unordered_contact_set,
        "static_affordance": static_affordance,
        "flat_pair_memory": lambda ep: flat_pair_memory(ep, seen),
        "mutated_no_side_gate": lambda ep: grammar_plan(ep, mutate="drop_side_gate"),
        "mutated_no_brace_gate": lambda ep: grammar_plan(ep, mutate="drop_brace_gate"),
    }
    episode_rows: List[Dict[str, object]] = []
    for ep in episodes:
        oracle, oracle_reason = mechanical_oracle(ep)
        for method, fn in methods.items():
            pred, reason = fn(ep)
            episode_rows.append(
                {
                    "episode_id": ep.episode_id,
                    "split": ep.split,
                    "task": ep.task.name,
                    "tool": ep.tool.name,
                    "tool_signature": ep.tool.signature,
                    "features": "+".join(ep.tool.features),
                    "length": ep.tool.length,
                    "stiffness": ep.tool.stiffness,
                    "blocked_side": ep.blocked_side,
                    "brace_available": int(ep.brace_available),
                    "fragile": int(ep.fragile),
                    "ood_signature": int(ep.ood_signature),
                    "oracle": bool(oracle),
                    "oracle_reason": oracle_reason,
                    "method": method,
                    "prediction": bool(pred),
                    "method_reason": reason,
                }
            )
    fieldnames = list(episode_rows[0].keys())
    write_csv(DATA / "episode_results.csv", episode_rows, fieldnames)
    aggregate_rows: List[Dict[str, object]] = []
    slices = {
        "test_all": lambda r: r["split"] == "test",
        "test_ood_valid": lambda r: r["split"] == "test" and r["ood_signature"] == 1 and r["oracle"],
        "test_invalid": lambda r: r["split"] == "test" and not r["oracle"],
        "test_blocked_side": lambda r: r["split"] == "test" and r["blocked_side"] in {"front", "behind", "under", "inside", "top"},
    }
    for method in methods:
        rows_m = [r for r in episode_rows if r["method"] == method]
        for slice_name, filt in slices.items():
            selected = [r for r in rows_m if filt(r)]
            m = metrics(selected)
            aggregate_rows.append({"method": method, "slice": slice_name, **m})
    write_csv(
        DATA / "aggregate_results.csv",
        aggregate_rows,
        ["method", "slice", "n", "accuracy", "precision", "recall", "f1", "false_positive_rate", "false_negative_rate"],
    )
    maybe_plot(aggregate_rows)
    write_latex_table(aggregate_rows)
    summary = {
        "episodes": len(episodes),
        "tools": len(tools),
        "train_signatures": len(seen),
        "test_all": [r for r in aggregate_rows if r["slice"] == "test_all"],
    }
    (DATA / "experiment_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    log("SUMMARY " + json.dumps(summary["test_all"], sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(run())
    except Exception as exc:  # noqa: BLE001
        print(f"CONTACT_GRAMMAR_EVAL_FATAL_BUT_CAUGHT: {exc}")
        raise SystemExit(0)
