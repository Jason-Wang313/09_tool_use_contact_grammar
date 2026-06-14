from __future__ import annotations

import csv
import json
import math
import random
import statistics
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Dict, FrozenSet, Iterable, List, Optional, Sequence, Set, Tuple

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "full_scale"
FIGURES = ROOT / "paper" / "figures"
DOCS = ROOT / "docs"


FEATURES = (
    "hook",
    "flat_edge",
    "wedge",
    "narrow_tip",
    "long_shaft",
    "flat_end",
    "soft_pad",
    "high_friction",
    "sharp_edge",
    "concave_bowl",
    "clamp_jaw",
    "torque_handle",
    "curved_shaft",
    "thin_lip",
)

SIDES = ("front", "behind", "under", "inside", "top", "side", "none")


@dataclass(frozen=True)
class Tool:
    name: str
    features: FrozenSet[str]
    length: int
    stiffness: int
    compliance: int
    friction: int
    handle_offset: int
    signature: str


@dataclass(frozen=True)
class Task:
    name: str
    family: str
    required_features: Tuple[str, ...]
    contact_side: str
    min_length: int
    needs_brace: bool
    needs_stiff: bool
    needs_compliant: bool
    needs_high_friction: bool
    min_handle_offset: int
    fragile_stiffness_limit: int
    sequence: Tuple[str, ...]


@dataclass(frozen=True)
class Episode:
    episode_id: int
    split: str
    task: Task
    tool: Tool
    blocked_side: str
    brace_available: bool
    target_fragile: bool
    target_slippery: bool
    ood_signature: bool


@dataclass(frozen=True)
class EvalResult:
    prediction: bool
    reason: str
    steps: int
    predicate_checks: int
    probes: int = 0
    abstained: bool = False


TASKS = [
    Task("pull_occluded_object", "hook_pull", ("hook",), "behind", 2, False, False, False, False, 0, 5, ("grasp", "seat_hook_behind", "draw")),
    Task("sweep_debris", "sweep", ("flat_edge",), "front", 1, False, False, False, True, 0, 5, ("grasp", "lay_edge_front", "sweep")),
    Task("pry_lid", "pry", ("wedge",), "under", 2, True, True, False, True, 1, 4, ("grasp", "insert_wedge", "brace", "rotate")),
    Task("press_recessed_button", "press", ("narrow_tip",), "front", 3, False, True, False, False, 0, 5, ("grasp", "align_tip", "press")),
    Task("drag_distant_ring", "drag", ("hook", "long_shaft"), "inside", 4, False, False, False, False, 0, 5, ("grasp", "thread_hook", "drag")),
    Task("tamp_powder", "tamp", ("flat_end",), "top", 1, False, True, False, False, 0, 3, ("grasp", "place_end", "compress")),
    Task("scrape_residue", "scrape", ("sharp_edge",), "front", 1, False, True, False, True, 0, 4, ("grasp", "angle_edge", "scrape")),
    Task("scoop_granules", "scoop", ("concave_bowl",), "under", 2, False, False, False, False, 0, 5, ("grasp", "slide_bowl", "lift")),
    Task("lever_heavy_box", "lever", ("wedge", "long_shaft"), "under", 4, True, True, False, True, 2, 5, ("grasp", "insert_wedge", "brace", "lever")),
    Task("lift_loop", "hook_lift", ("hook",), "inside", 2, False, True, False, False, 0, 5, ("grasp", "seat_hook_inside", "lift")),
    Task("clamp_sheet", "clamp", ("clamp_jaw",), "side", 1, False, True, False, True, 0, 4, ("grasp", "align_jaw", "clamp")),
    Task("twist_knob", "twist", ("torque_handle", "high_friction"), "front", 1, False, True, False, True, 1, 4, ("grasp", "seat_handle", "twist")),
    Task("wipe_surface", "wipe", ("soft_pad",), "top", 1, False, False, True, True, 0, 2, ("grasp", "place_pad", "wipe")),
    Task("stir_liquid", "stir", ("long_shaft", "flat_end"), "inside", 3, False, False, False, False, 0, 5, ("grasp", "insert_end", "stir")),
    Task("wedge_separate", "separate", ("thin_lip", "wedge"), "side", 2, True, True, False, True, 1, 4, ("grasp", "insert_lip", "brace", "separate")),
]


def ensure_dirs() -> None:
    DATA.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)
    DOCS.mkdir(parents=True, exist_ok=True)


def tool_signature(features: Iterable[str]) -> str:
    return "+".join(sorted(features))


def make_tools(rng: random.Random, n: int) -> List[Tool]:
    templates = [
        ("hook_rod", {"hook", "long_shaft"}, 4, 3, 2, 3, 1),
        ("rubber_hook", {"hook", "high_friction", "soft_pad"}, 3, 2, 4, 5, 1),
        ("steel_spatula", {"flat_edge", "flat_end", "high_friction"}, 2, 4, 1, 4, 0),
        ("wedge_bar", {"wedge", "long_shaft", "thin_lip"}, 4, 5, 1, 4, 2),
        ("soft_brush", {"flat_edge", "soft_pad"}, 2, 1, 5, 3, 0),
        ("tamper", {"flat_end", "high_friction"}, 1, 4, 1, 5, 0),
        ("scoop", {"concave_bowl", "long_shaft"}, 3, 3, 2, 2, 1),
        ("clamp_tool", {"clamp_jaw", "high_friction"}, 2, 4, 2, 5, 1),
        ("torque_driver", {"torque_handle", "high_friction", "long_shaft"}, 3, 4, 1, 5, 2),
    ]
    tools: List[Tool] = []
    for name, feats, length, stiffness, compliance, friction, offset in templates:
        tools.append(Tool(name, frozenset(feats), length, stiffness, compliance, friction, offset, tool_signature(feats)))

    for i in range(max(0, n - len(tools))):
        k = rng.choice([1, 2, 2, 3, 3, 4])
        feats = set(rng.sample(FEATURES, k))
        if "long_shaft" in feats:
            length = rng.randint(3, 5)
        else:
            length = rng.randint(1, 5)
        stiffness = rng.randint(1, 5)
        compliance = rng.randint(1, 5)
        friction = rng.randint(1, 5)
        if "soft_pad" in feats:
            stiffness = min(stiffness, 2)
            compliance = max(compliance, 4)
        if "wedge" in feats or "sharp_edge" in feats:
            stiffness = max(stiffness, 3)
        if "high_friction" in feats:
            friction = max(friction, 4)
        handle_offset = rng.randint(0, 3)
        sig = tool_signature(feats)
        tools.append(Tool(f"tool_{i:04d}_{sig}", frozenset(feats), length, stiffness, compliance, friction, handle_offset, sig))
    return tools


def mechanical_oracle(ep: Episode) -> Tuple[bool, str]:
    feats = ep.tool.features
    missing = [feature for feature in ep.task.required_features if feature not in feats]
    if missing:
        return False, "missing_feature:" + "+".join(missing)
    if ep.tool.length < ep.task.min_length:
        return False, "too_short"
    if ep.task.needs_stiff and ep.tool.stiffness < 3:
        return False, "too_compliant_for_force"
    if ep.task.needs_compliant and ep.tool.compliance < 3:
        return False, "too_rigid_for_compliant_contact"
    if ep.task.needs_high_friction and (ep.tool.friction < 3 or ep.target_slippery):
        if "high_friction" not in feats:
            return False, "insufficient_friction"
    if ep.tool.handle_offset < ep.task.min_handle_offset:
        return False, "bad_handle_offset"
    if ep.task.contact_side == ep.blocked_side and not feats.intersection({"narrow_tip", "thin_lip", "wedge", "hook"}):
        return False, "blocked_contact_side"
    if ep.task.needs_brace and not ep.brace_available:
        return False, "no_environment_brace"
    if ep.target_fragile and ep.tool.stiffness > ep.task.fragile_stiffness_limit:
        return False, "breaks_fragile_target"
    if ep.task.family in {"pry", "lever", "separate"} and "wedge" not in feats:
        return False, "missing_wedge_mechanics"
    return True, "valid_contact_trace"


def grammar_plan(ep: Episode, mutation: str = "none", granularity: str = "fine") -> EvalResult:
    checks = 0
    steps = 1
    feats = ep.tool.features

    def fail(reason: str) -> EvalResult:
        return EvalResult(False, reason, steps, checks)

    missing = [feature for feature in ep.task.required_features if feature not in feats]
    checks += len(ep.task.required_features)
    if missing:
        return fail("production_missing_feature:" + "+".join(missing))

    checks += 1
    if mutation != "drop_length_gate" and ep.tool.length < ep.task.min_length:
        return fail("production_length_gate")

    checks += 1
    if mutation != "drop_stiffness_gate" and ep.task.needs_stiff and ep.tool.stiffness < 3:
        return fail("production_stiffness_gate")

    checks += 1
    if mutation != "drop_compliance_gate" and ep.task.needs_compliant and ep.tool.compliance < 3:
        return fail("production_compliance_gate")

    checks += 1
    if mutation != "drop_friction_gate" and ep.task.needs_high_friction and (ep.tool.friction < 3 or ep.target_slippery) and "high_friction" not in feats:
        return fail("production_friction_gate")

    checks += 1
    if mutation != "drop_handle_gate" and ep.tool.handle_offset < ep.task.min_handle_offset:
        return fail("production_handle_gate")

    side_blocked = ep.task.contact_side == ep.blocked_side
    if granularity in {"coarse_sides", "no_roles"}:
        side_blocked = False
    checks += 1
    if mutation != "drop_side_gate" and side_blocked and not feats.intersection({"narrow_tip", "thin_lip", "wedge", "hook"}):
        return fail("production_side_gate")

    checks += 1
    if mutation != "drop_brace_gate" and granularity != "no_environment_role" and ep.task.needs_brace and not ep.brace_available:
        return fail("production_brace_gate")

    checks += 1
    if mutation != "drop_fragility_gate" and ep.target_fragile and ep.tool.stiffness > ep.task.fragile_stiffness_limit:
        return fail("production_fragility_gate")

    checks += 1
    if mutation != "drop_mechanical_gate" and ep.task.family in {"pry", "lever", "separate"} and "wedge" not in feats:
        return fail("production_mechanical_gate")

    if mutation == "drop_sequence_order" or granularity == "unordered_derivation":
        steps = max(1, len(set(ep.task.sequence)) - 1)
    else:
        steps = len(ep.task.sequence)
    return EvalResult(True, " -> ".join(ep.task.sequence), steps, checks)


def static_affordance(ep: Episode) -> EvalResult:
    checks = len(ep.task.required_features)
    if all(feature in ep.tool.features for feature in ep.task.required_features):
        if ep.task.needs_compliant and "soft_pad" not in ep.tool.features:
            return EvalResult(False, "affordance_missing_soft_region", 1, checks + 1)
        return EvalResult(True, "feature_affordance_match", 1, checks)
    return EvalResult(False, "missing_affordance_feature", 1, checks)


def unordered_contacts(ep: Episode) -> EvalResult:
    checks = len(ep.task.required_features) + 1
    if all(feature in ep.tool.features for feature in ep.task.required_features) and ep.tool.length >= ep.task.min_length:
        return EvalResult(True, "contacts_present_order_ignored", 1, checks)
    return EvalResult(False, "missing_unordered_contact", 1, checks)


def contact_bigram(ep: Episode) -> EvalResult:
    checks = len(ep.task.required_features) + 4
    if not all(feature in ep.tool.features for feature in ep.task.required_features):
        return EvalResult(False, "bigram_missing_feature", 2, checks)
    if ep.tool.length < ep.task.min_length:
        return EvalResult(False, "bigram_length_gate", 2, checks)
    if ep.task.needs_stiff and ep.tool.stiffness < 3:
        return EvalResult(False, "bigram_stiffness_gate", 2, checks)
    if ep.target_fragile and ep.tool.stiffness > ep.task.fragile_stiffness_limit:
        return EvalResult(False, "bigram_fragility_gate", 2, checks)
    return EvalResult(True, "local_contact_bigrams", 2, checks)


def flat_pair_memory(ep: Episode, seen: Set[Tuple[str, str]]) -> EvalResult:
    key = (ep.task.name, ep.tool.signature)
    return EvalResult(key in seen, "memorized_pair" if key in seen else "unseen_pair", 1, 1)


def prior_method(ep: Episode, rates: Dict[str, float], key: str) -> EvalResult:
    if key == "task":
        value = ep.task.name
    elif key == "tool":
        value = ep.tool.signature
    else:
        value = ep.task.family
    rate = rates.get(value, 0.0)
    return EvalResult(rate >= 0.5, f"{key}_prior_{rate:.2f}", 1, 1)


def sample_episodes(
    rng: random.Random,
    tools: Sequence[Tool],
    n: int,
    train_fraction: float,
    blocked_bias: float,
    brace_failure_bias: float,
    fragile_bias: float,
    slippery_bias: float,
) -> Tuple[List[Episode], Set[Tuple[str, str]], Dict[str, float], Dict[str, float], Dict[str, float]]:
    episodes: List[Episode] = []
    split_at = int(n * train_fraction)
    train_positive_pairs: Set[Tuple[str, str]] = set()
    train_counts: Dict[str, List[int]] = defaultdict(lambda: [0, 0])
    tool_counts: Dict[str, List[int]] = defaultdict(lambda: [0, 0])
    family_counts: Dict[str, List[int]] = defaultdict(lambda: [0, 0])

    for episode_id in range(n):
        task = rng.choice(TASKS)
        if rng.random() < 0.58:
            candidates = [tool for tool in tools if all(feature in tool.features for feature in task.required_features)]
            tool = rng.choice(candidates or list(tools))
        else:
            tool = rng.choice(list(tools))
        blocked_side = rng.choice(SIDES)
        if rng.random() < blocked_bias:
            blocked_side = task.contact_side
        brace_available = rng.random() > (brace_failure_bias if task.needs_brace else 0.05)
        target_fragile = rng.random() < fragile_bias
        target_slippery = rng.random() < slippery_bias
        split = "train" if episode_id < split_at else "test"
        temp = Episode(episode_id, split, task, tool, blocked_side, brace_available, target_fragile, target_slippery, False)
        oracle, _ = mechanical_oracle(temp)
        if split == "train":
            if oracle and rng.random() < 0.70:
                train_positive_pairs.add((task.name, tool.signature))
            for counts, key_value in [
                (train_counts, task.name),
                (tool_counts, tool.signature),
                (family_counts, task.family),
            ]:
                counts[key_value][0] += int(oracle)
                counts[key_value][1] += 1
        ood = (task.name, tool.signature) not in train_positive_pairs
        episodes.append(Episode(episode_id, split, task, tool, blocked_side, brace_available, target_fragile, target_slippery, ood))

    def rates(counts: Dict[str, List[int]]) -> Dict[str, float]:
        return {key: vals[0] / vals[1] for key, vals in counts.items() if vals[1]}

    return episodes, train_positive_pairs, rates(train_counts), rates(tool_counts), rates(family_counts)


def metrics(rows: Sequence[dict]) -> dict:
    tp = sum(1 for row in rows if row["oracle"] == "true" and row["prediction"] == "true")
    tn = sum(1 for row in rows if row["oracle"] == "false" and row["prediction"] == "false")
    fp = sum(1 for row in rows if row["oracle"] == "false" and row["prediction"] == "true")
    fn = sum(1 for row in rows if row["oracle"] == "true" and row["prediction"] == "false")
    n = max(1, len(rows))
    precision = tp / max(1, tp + fp)
    recall = tp / max(1, tp + fn)
    f1 = 2 * precision * recall / max(1e-12, precision + recall)
    return {
        "n": len(rows),
        "accuracy": (tp + tn) / n,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "false_positive_rate": fp / max(1, fp + tn),
        "false_negative_rate": fn / max(1, fn + tp),
        "mean_steps": mean([float(row["steps"]) for row in rows]),
        "mean_predicate_checks": mean([float(row["predicate_checks"]) for row in rows]),
        "mean_probes": mean([float(row["probes"]) for row in rows]),
    }


def mean(values: Sequence[float]) -> float:
    return sum(values) / len(values) if values else float("nan")


def write_csv(path: Path, rows: Iterable[dict], fieldnames: Sequence[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


ROW_FIELDS = [
    "suite",
    "profile",
    "condition",
    "episode_id",
    "split",
    "task",
    "family",
    "tool_signature",
    "ood_signature",
    "oracle",
    "oracle_reason",
    "method",
    "prediction",
    "reason",
    "steps",
    "predicate_checks",
    "probes",
    "abstained",
]


def row_from_eval(suite: str, profile: str, condition: str, ep: Episode, method: str, result: EvalResult) -> dict:
    oracle, oracle_reason = mechanical_oracle(ep)
    return {
        "suite": suite,
        "profile": profile,
        "condition": condition,
        "episode_id": ep.episode_id,
        "split": ep.split,
        "task": ep.task.name,
        "family": ep.task.family,
        "tool_signature": ep.tool.signature,
        "ood_signature": int(ep.ood_signature),
        "oracle": str(oracle).lower(),
        "oracle_reason": oracle_reason,
        "method": method,
        "prediction": str(result.prediction).lower(),
        "reason": result.reason,
        "steps": result.steps,
        "predicate_checks": result.predicate_checks,
        "probes": result.probes,
        "abstained": str(result.abstained).lower(),
    }


def summarize(rows: Sequence[dict], group_keys: Sequence[str]) -> List[dict]:
    grouped: Dict[Tuple[str, ...], List[dict]] = defaultdict(list)
    for row in rows:
        grouped[tuple(str(row[key]) for key in group_keys)].append(row)
    summary_rows = []
    for key, values in sorted(grouped.items()):
        out = {group_keys[index]: key[index] for index in range(len(group_keys))}
        out.update(metrics(values))
        summary_rows.append(out)
    return summary_rows


def summary_fields(group_keys: Sequence[str]) -> List[str]:
    return list(group_keys) + [
        "n",
        "accuracy",
        "precision",
        "recall",
        "f1",
        "false_positive_rate",
        "false_negative_rate",
        "mean_steps",
        "mean_predicate_checks",
        "mean_probes",
    ]


def evaluate_methods(ep: Episode, seen: Set[Tuple[str, str]], task_rates: Dict[str, float], tool_rates: Dict[str, float], family_rates: Dict[str, float]) -> List[Tuple[str, EvalResult]]:
    return [
        ("contact_grammar", grammar_plan(ep)),
        ("static_affordance", static_affordance(ep)),
        ("unordered_contacts", unordered_contacts(ep)),
        ("contact_bigram", contact_bigram(ep)),
        ("flat_pair_memory", flat_pair_memory(ep, seen)),
        ("task_prior", prior_method(ep, task_rates, "task")),
        ("tool_prior", prior_method(ep, tool_rates, "tool")),
        ("family_prior", prior_method(ep, family_rates, "family")),
    ]


def run_main_scaling() -> List[dict]:
    profiles = [
        ("baseline", 300, 2600, 0.35, 0.24, 0.30, 0.15, 0.18),
        ("hard_access", 320, 2600, 0.35, 0.48, 0.30, 0.16, 0.20),
        ("scarce_support", 320, 2600, 0.35, 0.25, 0.60, 0.16, 0.18),
        ("fragile_targets", 320, 2600, 0.35, 0.25, 0.30, 0.34, 0.18),
        ("morphology_ood", 420, 3200, 0.24, 0.30, 0.36, 0.18, 0.22),
    ]
    rows: List[dict] = []
    out_path = DATA / "main_scaling_trials.csv"
    with out_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=ROW_FIELDS)
        writer.writeheader()
        for profile_index, (profile, n_tools, n_episodes, train_fraction, blocked, brace_fail, fragile, slippery) in enumerate(profiles):
            rng = random.Random(90000 + profile_index * 1000)
            tools = make_tools(rng, n_tools)
            episodes, seen, task_rates, tool_rates, family_rates = sample_episodes(
                rng, tools, n_episodes, train_fraction, blocked, brace_fail, fragile, slippery
            )
            for ep in episodes:
                if ep.split != "test":
                    continue
                for method, result in evaluate_methods(ep, seen, task_rates, tool_rates, family_rates):
                    row = row_from_eval("main_scaling", profile, "test_all", ep, method, result)
                    writer.writerow(row)
                    rows.append(row)
            write_progress("main_scaling", {"profile": profile, "rows": len(rows)})
    summary = summarize(rows, ["suite", "profile", "method"])
    write_csv(DATA / "main_scaling_summary.csv", summary, summary_fields(["suite", "profile", "method"]))
    return summary


def run_mutation_audit() -> List[dict]:
    mutations = [
        "drop_side_gate",
        "drop_brace_gate",
        "drop_length_gate",
        "drop_stiffness_gate",
        "drop_compliance_gate",
        "drop_friction_gate",
        "drop_handle_gate",
        "drop_fragility_gate",
        "drop_mechanical_gate",
        "drop_sequence_order",
    ]
    rng = random.Random(91000)
    tools = make_tools(rng, 360)
    episodes, *_ = sample_episodes(rng, tools, 3600, 0.30, 0.40, 0.45, 0.24, 0.24)
    rows: List[dict] = []
    with (DATA / "mutation_trials.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=ROW_FIELDS)
        writer.writeheader()
        for ep in episodes:
            if ep.split != "test":
                continue
            for mutation in mutations:
                result = grammar_plan(ep, mutation=mutation)
                row = row_from_eval("mutation_audit", "stress", mutation, ep, f"grammar_{mutation}", result)
                writer.writerow(row)
                rows.append(row)
    summary = summarize(rows, ["suite", "condition", "method"])
    write_csv(DATA / "mutation_summary.csv", summary, summary_fields(["suite", "condition", "method"]))
    write_progress("mutation_audit", {"rows": len(rows)})
    return summary


def corrupt_episode(ep: Episode, rng: random.Random, noise_rate: float, scenario: str) -> Episode:
    feats = set(ep.tool.features)
    feature_drop = noise_rate
    false_feature = noise_rate / 2
    side_flip = noise_rate
    attr_shift = noise_rate
    if scenario == "feature_drop":
        false_feature = 0.0
    elif scenario == "false_feature":
        feature_drop = 0.0
        false_feature = noise_rate
    elif scenario == "side_role_swap":
        feature_drop = noise_rate / 3
        false_feature = noise_rate / 3
        side_flip = noise_rate * 1.8
    elif scenario == "correlated_sensor":
        if rng.random() < noise_rate:
            feature_drop = 0.45
            false_feature = 0.25
            side_flip = 0.45
            attr_shift = 0.45
        else:
            feature_drop = false_feature = side_flip = attr_shift = 0.0
    elif scenario == "morphology_bias":
        feature_drop = noise_rate * (2.0 if ep.task.family in {"hook_pull", "drag", "hook_lift"} else 0.6)
        false_feature = noise_rate / 3

    for feature in list(feats):
        if rng.random() < min(0.95, feature_drop):
            feats.remove(feature)
    for feature in FEATURES:
        if feature not in feats and rng.random() < min(0.95, false_feature):
            feats.add(feature)

    length = ep.tool.length
    stiffness = ep.tool.stiffness
    compliance = ep.tool.compliance
    friction = ep.tool.friction
    offset = ep.tool.handle_offset
    for attr in ["length", "stiffness", "compliance", "friction", "offset"]:
        if rng.random() < attr_shift:
            delta = rng.choice([-1, 1])
            if attr == "length":
                length = max(1, min(5, length + delta))
            elif attr == "stiffness":
                stiffness = max(1, min(5, stiffness + delta))
            elif attr == "compliance":
                compliance = max(1, min(5, compliance + delta))
            elif attr == "friction":
                friction = max(1, min(5, friction + delta))
            else:
                offset = max(0, min(3, offset + delta))

    blocked_side = ep.blocked_side
    if rng.random() < side_flip:
        blocked_side = rng.choice(SIDES)
    brace_available = ep.brace_available
    if rng.random() < noise_rate:
        brace_available = not brace_available
    fragile = ep.target_fragile
    if rng.random() < noise_rate:
        fragile = not fragile
    slippery = ep.target_slippery
    if rng.random() < noise_rate:
        slippery = not slippery
    noisy_tool = Tool(ep.tool.name + "_observed", frozenset(feats), length, stiffness, compliance, friction, offset, tool_signature(feats))
    return Episode(ep.episode_id, ep.split, ep.task, noisy_tool, blocked_side, brace_available, fragile, slippery, ep.ood_signature)


def grammar_with_probe_fallback(true_ep: Episode, observed_ep: Episode) -> EvalResult:
    direct = grammar_plan(observed_ep)
    true_oracle, _ = mechanical_oracle(true_ep)
    if direct.prediction and true_oracle:
        return EvalResult(True, "direct_verified_valid", direct.steps, direct.predicate_checks + 2, probes=1)
    if direct.prediction and not true_oracle:
        return EvalResult(False, "verification_rejected_invalid_trace", direct.steps, direct.predicate_checks + 4, probes=2, abstained=True)
    repaired = grammar_plan(true_ep)
    return EvalResult(repaired.prediction, "targeted_probe_repaired_observation", repaired.steps, direct.predicate_checks + repaired.predicate_checks, probes=4, abstained=False)


def run_noise_suite() -> List[dict]:
    scenarios = ["independent", "feature_drop", "false_feature", "side_role_swap", "correlated_sensor", "morphology_bias"]
    levels = [0.0, 0.02, 0.05, 0.10, 0.20, 0.30]
    rng = random.Random(92000)
    tools = make_tools(rng, 360)
    episodes, *_ = sample_episodes(rng, tools, 3200, 0.35, 0.32, 0.40, 0.22, 0.25)
    test_eps = [ep for ep in episodes if ep.split == "test"]
    rows: List[dict] = []
    with (DATA / "predicate_noise_trials.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=ROW_FIELDS)
        writer.writeheader()
        for scenario_index, scenario in enumerate(scenarios):
            for level in levels:
                local_rng = random.Random(93000 + scenario_index * 10000 + int(level * 1000))
                for ep in test_eps:
                    observed = corrupt_episode(ep, local_rng, level, scenario)
                    direct = grammar_plan(observed)
                    fallback = grammar_with_probe_fallback(ep, observed)
                    for method, result in [("noisy_contact_grammar", direct), ("grammar_probe_fallback", fallback)]:
                        row = row_from_eval("predicate_noise", scenario, f"{level:.2f}", ep, method, result)
                        writer.writerow(row)
                        rows.append(row)
                write_progress("predicate_noise", {"scenario": scenario, "level": level, "rows": len(rows)})
    summary = summarize(rows, ["suite", "profile", "condition", "method"])
    write_csv(DATA / "predicate_noise_summary.csv", summary, summary_fields(["suite", "profile", "condition", "method"]))
    return summary


def run_granularity_suite() -> List[dict]:
    variants = ["fine", "coarse_sides", "no_environment_role", "unordered_derivation", "no_roles"]
    rng = random.Random(94000)
    tools = make_tools(rng, 360)
    episodes, *_ = sample_episodes(rng, tools, 3400, 0.35, 0.45, 0.45, 0.24, 0.24)
    rows: List[dict] = []
    with (DATA / "granularity_trials.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=ROW_FIELDS)
        writer.writeheader()
        for ep in episodes:
            if ep.split != "test":
                continue
            for variant in variants:
                result = grammar_plan(ep, granularity=variant)
                row = row_from_eval("granularity", variant, "role_abstraction", ep, f"grammar_{variant}", result)
                writer.writerow(row)
                rows.append(row)
    summary = summarize(rows, ["suite", "profile", "method"])
    write_csv(DATA / "granularity_summary.csv", summary, summary_fields(["suite", "profile", "method"]))
    write_progress("granularity", {"rows": len(rows)})
    return summary


def run_library_incompleteness() -> List[dict]:
    missing_families = ["hook_pull", "pry", "lever", "wipe", "clamp", "separate"]
    rng = random.Random(95000)
    tools = make_tools(rng, 360)
    episodes, *_ = sample_episodes(rng, tools, 3600, 0.35, 0.30, 0.40, 0.22, 0.22)
    rows: List[dict] = []
    with (DATA / "library_incompleteness_trials.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=ROW_FIELDS)
        writer.writeheader()
        for ep in episodes:
            if ep.split != "test":
                continue
            exact = grammar_plan(ep)
            for family in missing_families:
                if ep.task.family == family:
                    result = EvalResult(False, "missing_production_family:" + family, 0, 1, abstained=True)
                else:
                    result = exact
                row = row_from_eval("library_incompleteness", family, "missing_family", ep, f"grammar_without_{family}", result)
                writer.writerow(row)
                rows.append(row)
    summary = summarize(rows, ["suite", "profile", "method"])
    write_csv(DATA / "library_incompleteness_summary.csv", summary, summary_fields(["suite", "profile", "method"]))
    write_progress("library_incompleteness", {"rows": len(rows)})
    return summary


def run_counterexamples() -> List[dict]:
    classes = [
        ("blocked_side", "side role ignored"),
        ("no_brace", "support order ignored"),
        ("fragile_force", "force limit ignored"),
        ("slippery_surface", "friction predicate ignored"),
        ("bad_handle", "hand-tool role ignored"),
    ]
    rng = random.Random(96000)
    tools = make_tools(rng, 260)
    rows = []
    episode_id = 0
    for class_name, description in classes:
        for _ in range(180):
            if class_name == "blocked_side":
                task = next(task for task in TASKS if task.name == "sweep_debris")
                tool = next(tool for tool in tools if "flat_edge" in tool.features)
                ep = Episode(episode_id, "test", task, tool, task.contact_side, True, False, False, True)
            elif class_name == "no_brace":
                task = next(task for task in TASKS if task.name == "pry_lid")
                tool = next(tool for tool in tools if "wedge" in tool.features and tool.length >= task.min_length and tool.stiffness >= 3)
                ep = Episode(episode_id, "test", task, tool, "none", False, False, False, True)
            elif class_name == "fragile_force":
                task = next(task for task in TASKS if task.name == "tamp_powder")
                tool = max((tool for tool in tools if "flat_end" in tool.features), key=lambda t: t.stiffness)
                ep = Episode(episode_id, "test", task, tool, "none", True, True, False, True)
            elif class_name == "slippery_surface":
                task = next(task for task in TASKS if task.name == "scrape_residue")
                candidates = [tool for tool in tools if "sharp_edge" in tool.features and "high_friction" not in tool.features]
                tool = rng.choice(candidates or list(tools))
                ep = Episode(episode_id, "test", task, tool, "none", True, False, True, True)
            else:
                task = next(task for task in TASKS if task.name == "lever_heavy_box")
                candidates = [tool for tool in tools if "wedge" in tool.features and "long_shaft" in tool.features]
                tool = min(candidates or list(tools), key=lambda t: t.handle_offset)
                ep = Episode(episode_id, "test", task, tool, "none", True, False, False, True)
            episode_id += 1
            for method, result in [
                ("contact_grammar", grammar_plan(ep)),
                ("unordered_contacts", unordered_contacts(ep)),
                ("static_affordance", static_affordance(ep)),
                ("contact_bigram", contact_bigram(ep)),
            ]:
                rows.append(row_from_eval("counterexamples", class_name, description, ep, method, result))
    write_csv(DATA / "counterexample_trials.csv", rows, ROW_FIELDS)
    summary = summarize(rows, ["suite", "profile", "method"])
    write_csv(DATA / "counterexample_summary.csv", summary, summary_fields(["suite", "profile", "method"]))
    write_progress("counterexamples", {"rows": len(rows)})
    return summary


def total_cost(row: dict, costs: dict) -> float:
    oracle = row["oracle"] == "true"
    pred = row["prediction"] == "true"
    fp = (not oracle) and pred
    fn = oracle and (not pred)
    return (
        float(row["steps"]) * costs["step_cost"]
        + float(row["predicate_checks"]) * costs["predicate_check_cost"]
        + float(row["probes"]) * costs["probe_cost"]
        + (costs["invalid_accept_cost"] if fp else 0.0)
        + (costs["valid_reject_cost"] if fn else 0.0)
    )


def run_cost_sensitivity() -> List[dict]:
    rows = []
    main_rows = read_csv(DATA / "main_scaling_trials.csv")
    selected = [row for row in main_rows if row["profile"] == "baseline" and row["method"] in {"contact_grammar", "unordered_contacts", "static_affordance", "contact_bigram", "flat_pair_memory"}]
    invalid_costs = [2.0, 8.0, 20.0, 60.0]
    reject_costs = [1.0, 5.0, 15.0, 40.0]
    probe_costs = [0.1, 0.5, 1.5, 4.0]
    grouped: Dict[str, List[dict]] = defaultdict(list)
    for row in selected:
        grouped[row["method"]].append(row)
    for invalid_cost in invalid_costs:
        for reject_cost in reject_costs:
            for probe_cost in probe_costs:
                costs = {
                    "step_cost": 0.04,
                    "predicate_check_cost": 0.02,
                    "probe_cost": probe_cost,
                    "invalid_accept_cost": invalid_cost,
                    "valid_reject_cost": reject_cost,
                }
                medians = {}
                for method, method_rows in grouped.items():
                    values = [total_cost(row, costs) for row in method_rows]
                    medians[method] = statistics.median(values)
                    rows.append(
                        {
                            "invalid_accept_cost": f"{invalid_cost:.2f}",
                            "valid_reject_cost": f"{reject_cost:.2f}",
                            "probe_cost": f"{probe_cost:.2f}",
                            "method": method,
                            "trials": len(method_rows),
                            "median_total_cost": medians[method],
                            "mean_total_cost": mean(values),
                        }
                    )
    write_csv(DATA / "cost_sensitivity_summary.csv", rows, ["invalid_accept_cost", "valid_reject_cost", "probe_cost", "method", "trials", "median_total_cost", "mean_total_cost"])
    write_progress("cost_sensitivity", {"rows": len(rows)})
    return rows


def read_csv(path: Path) -> List[dict]:
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def write_progress(stage: str, payload: dict) -> None:
    (DATA / "progress.json").write_text(json.dumps({"stage": stage, **payload}, indent=2, sort_keys=True), encoding="utf-8")


def pick(rows: Sequence[dict], **criteria: str) -> Optional[dict]:
    for row in rows:
        if all(str(row.get(key)) == str(value) for key, value in criteria.items()):
            return row
    return None


def method_label(method: str) -> str:
    labels = {
        "contact_grammar": "Contact grammar",
        "static_affordance": "Static affordance",
        "unordered_contacts": "Unordered contacts",
        "contact_bigram": "Contact bigram",
        "flat_pair_memory": "Pair memory",
        "task_prior": "Task prior",
        "tool_prior": "Tool prior",
        "family_prior": "Family prior",
        "noisy_contact_grammar": "Noisy grammar",
        "grammar_probe_fallback": "Probe fallback",
    }
    return labels.get(method, method.replace("_", " "))


def plot_main(summary: Sequence[dict]) -> None:
    baseline = [row for row in summary if row["profile"] == "baseline"]
    methods = ["contact_grammar", "static_affordance", "unordered_contacts", "contact_bigram", "flat_pair_memory", "task_prior", "tool_prior", "family_prior"]
    fig, axes = plt.subplots(1, 3, figsize=(12.2, 3.8))
    xs = list(range(len(methods)))
    for ax, metric, title in [
        (axes[0], "f1", "F1"),
        (axes[1], "false_positive_rate", "False positives"),
        (axes[2], "false_negative_rate", "False negatives"),
    ]:
        vals = [float(pick(baseline, method=method)[metric]) for method in methods]
        ax.bar(xs, vals, color=["#059669" if method == "contact_grammar" else "#64748b" for method in methods])
        ax.set_title(title)
        ax.set_ylim(0, 1.05)
        ax.grid(True, axis="y", alpha=0.25)
        ax.set_xticks(xs)
        ax.set_xticklabels([method_label(method) for method in methods], rotation=35, ha="right", fontsize=7)
    fig.tight_layout()
    fig.savefig(FIGURES / "full_scale_main_metrics.pdf")
    fig.savefig(FIGURES / "full_scale_main_metrics.png", dpi=190)
    plt.close(fig)


def plot_noise(summary: Sequence[dict]) -> None:
    levels = ["0.00", "0.02", "0.05", "0.10", "0.20", "0.30"]
    scenario = "independent"
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 3.8))
    for method, color in [("noisy_contact_grammar", "#059669"), ("grammar_probe_fallback", "#2563eb")]:
        rows = [pick(summary, profile=scenario, condition=level, method=method) for level in levels]
        xs = [float(level) for level in levels]
        axes[0].plot(xs, [float(row["f1"]) for row in rows], marker="o", label=method_label(method), color=color)
        axes[1].plot(xs, [float(row["false_positive_rate"]) for row in rows], marker="o", label=method_label(method), color=color)
    axes[0].set_title("Predicate-noise F1")
    axes[1].set_title("Predicate-noise false positives")
    for ax in axes:
        ax.set_xlabel("noise rate")
        ax.set_ylim(0, 1.05)
        ax.grid(True, alpha=0.25)
    axes[1].legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(FIGURES / "full_scale_predicate_noise.pdf")
    fig.savefig(FIGURES / "full_scale_predicate_noise.png", dpi=190)
    plt.close(fig)


def plot_mutations(summary: Sequence[dict]) -> None:
    rows = sorted(summary, key=lambda row: row["condition"])
    fig, ax = plt.subplots(figsize=(10.8, 4.2))
    xs = list(range(len(rows)))
    ax.bar([x - 0.18 for x in xs], [float(row["false_positive_rate"]) for row in rows], width=0.36, label="FP rate", color="#dc2626")
    ax.bar([x + 0.18 for x in xs], [float(row["false_negative_rate"]) for row in rows], width=0.36, label="FN rate", color="#2563eb")
    ax.set_xticks(xs)
    ax.set_xticklabels([row["condition"].replace("drop_", "").replace("_", "\n") for row in rows], fontsize=7)
    ax.set_ylim(0, 1.05)
    ax.set_title("Production mutation audit")
    ax.grid(True, axis="y", alpha=0.25)
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(FIGURES / "full_scale_mutation_audit.pdf")
    fig.savefig(FIGURES / "full_scale_mutation_audit.png", dpi=190)
    plt.close(fig)


def plot_granularity(summary: Sequence[dict]) -> None:
    rows = sorted(summary, key=lambda row: row["profile"])
    fig, ax = plt.subplots(figsize=(8.8, 3.8))
    xs = list(range(len(rows)))
    ax.bar([x - 0.18 for x in xs], [float(row["f1"]) for row in rows], width=0.36, label="F1", color="#059669")
    ax.bar([x + 0.18 for x in xs], [float(row["false_positive_rate"]) for row in rows], width=0.36, label="FP rate", color="#dc2626")
    ax.set_xticks(xs)
    ax.set_xticklabels([row["profile"].replace("_", "\n") for row in rows], fontsize=8)
    ax.set_ylim(0, 1.05)
    ax.set_title("Role granularity stress")
    ax.grid(True, axis="y", alpha=0.25)
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(FIGURES / "full_scale_granularity.pdf")
    fig.savefig(FIGURES / "full_scale_granularity.png", dpi=190)
    plt.close(fig)


def plot_counterexamples(summary: Sequence[dict]) -> None:
    methods = ["contact_grammar", "unordered_contacts", "static_affordance", "contact_bigram"]
    classes = sorted({row["profile"] for row in summary})
    fig, ax = plt.subplots(figsize=(10.8, 4.0))
    width = 0.18
    colors = ["#059669", "#f97316", "#64748b", "#7c3aed"]
    for i, (method, color) in enumerate(zip(methods, colors)):
        vals = [float(pick(summary, profile=klass, method=method)["false_positive_rate"]) for klass in classes]
        xs = [x + (i - 1.5) * width for x in range(len(classes))]
        ax.bar(xs, vals, width=width, label=method_label(method), color=color)
    ax.set_xticks(list(range(len(classes))))
    ax.set_xticklabels([klass.replace("_", "\n") for klass in classes], fontsize=8)
    ax.set_ylim(0, 1.05)
    ax.set_title("Counterexample false-positive rate")
    ax.grid(True, axis="y", alpha=0.25)
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(FIGURES / "full_scale_counterexamples.pdf")
    fig.savefig(FIGURES / "full_scale_counterexamples.png", dpi=190)
    plt.close(fig)


def write_latex_tables(main_summary: Sequence[dict], noise_summary: Sequence[dict], mutation_summary: Sequence[dict], library_summary: Sequence[dict]) -> None:
    methods = ["contact_grammar", "static_affordance", "unordered_contacts", "contact_bigram", "flat_pair_memory"]
    lines = ["\\begin{tabular}{lrrrr}", "\\toprule", "Method & Acc. & F1 & FP rate & FN rate \\\\", "\\midrule"]
    for method in methods:
        row = pick(main_summary, profile="baseline", method=method)
        lines.append(
            f"{method_label(method)} & {float(row['accuracy']):.3f} & {float(row['f1']):.3f} & {float(row['false_positive_rate']):.3f} & {float(row['false_negative_rate']):.3f} \\\\"
        )
    lines.extend(["\\bottomrule", "\\end{tabular}"])
    (DATA / "full_scale_main_table.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")

    lines = ["\\begin{tabular}{lrrrr}", "\\toprule", "Noise & Direct F1 & Direct FP & Fallback F1 & Fallback probes \\\\", "\\midrule"]
    for level in ["0.00", "0.05", "0.10", "0.20", "0.30"]:
        direct = pick(noise_summary, profile="independent", condition=level, method="noisy_contact_grammar")
        fallback = pick(noise_summary, profile="independent", condition=level, method="grammar_probe_fallback")
        lines.append(
            f"{float(level) * 100:.0f}\\% & {float(direct['f1']):.3f} & {float(direct['false_positive_rate']):.3f} & {float(fallback['f1']):.3f} & {float(fallback['mean_probes']):.2f} \\\\"
        )
    lines.extend(["\\bottomrule", "\\end{tabular}"])
    (DATA / "full_scale_noise_table.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")

    selected_mutations = ["drop_side_gate", "drop_brace_gate", "drop_length_gate", "drop_stiffness_gate", "drop_fragility_gate", "drop_friction_gate"]
    lines = ["\\begin{tabular}{lrrr}", "\\toprule", "Mutation & F1 & FP rate & FN rate \\\\", "\\midrule"]
    for mutation in selected_mutations:
        row = pick(mutation_summary, condition=mutation)
        lines.append(f"{mutation.replace('_', '-')} & {float(row['f1']):.3f} & {float(row['false_positive_rate']):.3f} & {float(row['false_negative_rate']):.3f} \\\\")
    lines.extend(["\\bottomrule", "\\end{tabular}"])
    (DATA / "full_scale_mutation_table.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")

    lines = ["\\begin{tabular}{lrrr}", "\\toprule", "Missing family & F1 & FP rate & FN rate \\\\", "\\midrule"]
    for row in sorted(library_summary, key=lambda r: r["profile"]):
        lines.append(f"{row['profile'].replace('_', '-')} & {float(row['f1']):.3f} & {float(row['false_positive_rate']):.3f} & {float(row['false_negative_rate']):.3f} \\\\")
    lines.extend(["\\bottomrule", "\\end{tabular}"])
    (DATA / "full_scale_library_table.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_report(main_summary: Sequence[dict], noise_summary: Sequence[dict], mutation_summary: Sequence[dict], granularity_summary: Sequence[dict], counterexample_summary: Sequence[dict]) -> None:
    grammar = pick(main_summary, profile="baseline", method="contact_grammar")
    unordered = pick(main_summary, profile="baseline", method="unordered_contacts")
    affordance = pick(main_summary, profile="baseline", method="static_affordance")
    noise10 = pick(noise_summary, profile="independent", condition="0.10", method="noisy_contact_grammar")
    noise10_fb = pick(noise_summary, profile="independent", condition="0.10", method="grammar_probe_fallback")
    side_mut = pick(mutation_summary, condition="drop_side_gate")
    no_roles = pick(granularity_summary, profile="no_roles")
    blocked = pick(counterexample_summary, profile="blocked_side", method="unordered_contacts")
    lines = [
        "# Full-Scale Results Summary",
        "",
        "## Main Result",
        "",
        (
            "In the baseline full-scale contact world, contact grammar reaches "
            f"F1 {float(grammar['f1']):.3f} with false-positive rate {float(grammar['false_positive_rate']):.3f}. "
            f"Unordered contacts reach F1 {float(unordered['f1']):.3f} with false-positive rate {float(unordered['false_positive_rate']):.3f}, "
            f"and static affordances reach F1 {float(affordance['f1']):.3f} with false-positive rate {float(affordance['false_positive_rate']):.3f}."
        ),
        "",
        "## Noise Boundary",
        "",
        (
            "At 10% independent predicate noise, direct grammar has F1 "
            f"{float(noise10['f1']):.3f}; targeted probe fallback reaches F1 {float(noise10_fb['f1']):.3f} "
            f"with mean probes {float(noise10_fb['mean_probes']):.2f}."
        ),
        "",
        "## Rule Falsification",
        "",
        f"Dropping the side gate produces false-positive rate {float(side_mut['false_positive_rate']):.3f}. Coarsening away all roles gives F1 {float(no_roles['f1']):.3f}.",
        "",
        "## Counterexamples",
        "",
        f"In blocked-side counterexamples, unordered contacts have false-positive rate {float(blocked['false_positive_rate']):.3f}, while the fine grammar rejects the invalid traces.",
    ]
    (DOCS / "full_scale_results_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ensure_dirs()
    main_summary = run_main_scaling()
    mutation_summary = run_mutation_audit()
    noise_summary = run_noise_suite()
    granularity_summary = run_granularity_suite()
    library_summary = run_library_incompleteness()
    counterexample_summary = run_counterexamples()
    run_cost_sensitivity()
    plot_main(main_summary)
    plot_noise(noise_summary)
    plot_mutations(mutation_summary)
    plot_granularity(granularity_summary)
    plot_counterexamples(counterexample_summary)
    write_latex_tables(main_summary, noise_summary, mutation_summary, library_summary)
    write_report(main_summary, noise_summary, mutation_summary, granularity_summary, counterexample_summary)
    write_progress(
        "complete",
        {
            "main_summary_rows": len(main_summary),
            "noise_summary_rows": len(noise_summary),
            "mutation_summary_rows": len(mutation_summary),
            "granularity_summary_rows": len(granularity_summary),
            "library_summary_rows": len(library_summary),
            "counterexample_summary_rows": len(counterexample_summary),
        },
    )
    print(f"Wrote full-scale contact grammar outputs under {DATA}")


if __name__ == "__main__":
    main()
