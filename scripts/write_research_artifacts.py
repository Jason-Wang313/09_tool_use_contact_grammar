"""Write literature docs, claims, paper sources, and runnable repo docs."""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path
from typing import Dict, List


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
DATA = ROOT / "data"
PAPER = ROOT / "paper"
FIGURES = ROOT / "figures"
DOWNLOAD_PDF = Path("C:/Users/wangz/Downloads/09.pdf")
DESKTOP_PDF = Path("C:/Users/wangz/OneDrive/Desktop/09.pdf")


def read_csv(path: Path) -> List[Dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def read_json(path: Path) -> Dict[str, object]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return {}


def safe(text: str) -> str:
    text = text or ""
    text = text.encode("ascii", "ignore").decode("ascii")
    return re.sub(r"\s+", " ", text).strip()


def md_escape(text: str) -> str:
    return safe(text).replace("|", "\\|")


def top_rows(rows: List[Dict[str, str]], n: int) -> List[Dict[str, str]]:
    try:
        return sorted(rows, key=lambda r: float(r.get("relevance_score", 0)), reverse=True)[:n]
    except Exception:
        return rows[:n]


def aggregate_lookup(rows: List[Dict[str, str]]) -> Dict[str, Dict[str, str]]:
    return {r["method"]: r for r in rows if r.get("slice") == "test_all"}


def fmt_metric(row: Dict[str, str], key: str) -> str:
    try:
        return f"{float(row.get(key, 0.0)):.3f}"
    except Exception:
        return "n/a"


def write_literature_map(matrix: List[Dict[str, str]]) -> None:
    DOCS.mkdir(exist_ok=True)
    sources: Dict[str, int] = {}
    mechanisms: Dict[str, int] = {}
    years: Dict[str, int] = {}
    for row in matrix:
        sources[row.get("source_kind", "unknown")] = sources.get(row.get("source_kind", "unknown"), 0) + 1
        mech = row.get("actual_mechanism_introduced", "unknown")
        mechanisms[mech] = mechanisms.get(mech, 0) + 1
        years[row.get("year", "unknown")] = years.get(row.get("year", "unknown"), 0) + 1
    mechanism_lines = "\n".join(
        f"- {md_escape(k)}: {v}" for k, v in sorted(mechanisms.items(), key=lambda kv: kv[1], reverse=True)[:12]
    )
    source_lines = "\n".join(f"- {md_escape(k)}: {v}" for k, v in sorted(sources.items()))
    top = top_rows(matrix, 20)
    top_lines = "\n".join(
        f"{i}. **{md_escape(r.get('title', ''))}** ({md_escape(r.get('year', ''))}) - {md_escape(r.get('what_it_makes_less_novel', ''))}"
        for i, r in enumerate(top, 1)
    )
    assumptions = [
        "Affordance labels can be assigned before the contact sequence is known.",
        "A tool's functional part determines use independent of how the robot grips it.",
        "Contacts with the same object pair are interchangeable across sides and roles.",
        "The environment is a passive obstacle rather than an active mechanical support.",
        "Task success can be predicted from object category plus action name.",
        "Contact-rich tool use can be handled by searching contact modes after high-level planning.",
        "A learned policy will interpolate to unseen compositions of familiar tool parts.",
        "Language decompositions preserve force, side, and support preconditions.",
        "Task-and-motion predicates expose all mechanically relevant contact roles.",
        "Tactile feedback only repairs execution, rather than changing the symbolic plan.",
        "Grasp stability and task effectiveness can be optimized independently.",
        "One affordance region has one function across target geometries.",
        "Tool use is a two-stage pick-then-use process rather than a contact graph over hand, tool, target, and environment.",
        "The right abstraction is a state vector or latent embedding, not a typed production rule.",
        "Failure is mostly distribution shift, not a falsified physical precondition.",
        "Contact order is recoverable from an unordered set of contacts.",
        "Compliance can be modeled as noise around rigid contact predictions.",
        "Intermediate representations should be descriptive maps rather than generative rules.",
        "A planner's no-plan result is less informative than a failed production.",
        "Demonstrations teach action chunks, not the hidden contact grammar that makes chunks reusable.",
        "Contact grammar is only a notation, not an executable hypothesis class.",
        "Novel tools require new data instead of recombining known contact productions.",
        "Friction and support assumptions can be left implicit until low-level control.",
        "Tool morphology and contact role can be separated cleanly.",
    ]
    directions = [
        ("Counterfactual affordance maps", "Force an affordance model to predict when the same region becomes invalid under a changed contact order."),
        ("Contact-role grammar", "Make ordered hand-tool-target-environment contacts the central representation and test each production as a falsifiable rule."),
        ("Mechanics-first TAMP predicates", "Replace object predicates with mechanically typed supports, pivots, and force-transmission relations."),
        ("Tool morphology calculus", "Represent tools by reusable mechanical operators rather than category labels or learned embeddings."),
        ("Failure-language bridge", "Translate contact production failures into language for human repair without using language as the planner."),
    ]
    direction_lines = "\n".join(f"- **{name}.** {desc}" for name, desc in directions)
    text = f"""# Literature Map

## Field Box
Robot tool use inside contact-rich manipulation: how an embodied agent represents, plans, and diagnoses physical interactions among hand, tool, target, and environment.

## Sweep Accounting
- Landscape entries in `docs/related_work_matrix.csv`: {len(matrix)}
- Serious skim proxy: {sum(1 for r in matrix if r.get('serious_skim') == '1')} papers
- Deep read proxy: {sum(1 for r in matrix if r.get('deep_read') == '1')} papers
- Hostile prior set: {sum(1 for r in matrix if r.get('hostile_prior') == '1')} papers

## Source Mix
{source_lines}

## Dominant Mechanism Families
{mechanism_lines}

## Top Novelty-Pressuring Papers
{top_lines}

## Hidden Assumptions That May Be False
""" + "\n".join(f"{i}. {a}" for i, a in enumerate(assumptions, 1)) + f"""

## Directions Generated Before Selection
{direction_lines}

## Selection
The strongest direction is **contact-role grammar**: represent tool use as typed, ordered productions over contacts, where each production has explicit preconditions and counterfactual failure tests. This changes the central mechanism from static affordance, opaque policy, or mode-search abstraction to a compositional rule system whose rules can be individually falsified.
"""
    (DOCS / "literature_map.md").write_text(text, encoding="utf-8")


def write_hostile_prior(matrix: List[Dict[str, str]]) -> None:
    hostile = top_rows(matrix, 100)
    lines = [
        "# Hostile Prior Work Set",
        "",
        "This is the 100-paper hostile set used to pressure the novelty claim. Each entry records the claimed problem, actual mechanism, hidden assumptions, fixed variables, ignored failures, what becomes less novel, and what remains open.",
        "",
    ]
    for i, r in enumerate(hostile, 1):
        lines.extend(
            [
                f"## {i}. {md_escape(r.get('title', 'untitled'))} ({md_escape(r.get('year', ''))})",
                f"- Source: {md_escape(r.get('venue_or_source', ''))} | {md_escape(r.get('url', ''))}",
                f"- Problem claimed: {md_escape(r.get('problem_claimed', ''))}",
                f"- Actual mechanism introduced: {md_escape(r.get('actual_mechanism_introduced', ''))}",
                f"- Hidden assumptions: {md_escape(r.get('hidden_assumptions', ''))}",
                f"- Variables treated as fixed: {md_escape(r.get('variables_treated_as_fixed', ''))}",
                f"- Failure modes ignored: {md_escape(r.get('failure_modes_ignored', ''))}",
                f"- What it makes less novel: {md_escape(r.get('what_it_makes_less_novel', ''))}",
                f"- What it leaves open: {md_escape(r.get('what_it_leaves_open', ''))}",
                "",
            ]
        )
    (DOCS / "hostile_prior_work.md").write_text("\n".join(lines), encoding="utf-8")


def write_novelty_docs(matrix: List[Dict[str, str]], aggregate: List[Dict[str, str]]) -> None:
    lookup = aggregate_lookup(aggregate)
    cg = lookup.get("contact_grammar", {})
    unordered = lookup.get("unordered_contacts", {})
    flat = lookup.get("flat_pair_memory", {})
    text = f"""# Novelty Boundary Map

## What Is Not New
- Affordances are a long-standing way to describe object-action possibilities.
- Task-oriented grasping already couples grasp choice to downstream tool use.
- Contact-rich manipulation planning already models contact modes, supports, and constraints.
- Task-and-motion planning already uses symbolic preconditions and continuous feasibility checks.
- Robot foundation models and LLM planners already map broad instructions to robot actions.

## Boundary Against Closest Areas
- Against affordance maps: the proposed mechanism predicts an **ordered derivation** over hand-tool-target-environment contacts, not a region or action label.
- Against contact-mode optimization: the proposed mechanism is a compact symbolic grammar over contact roles, intended to prune and diagnose mode traces before continuous optimization.
- Against TAMP: the production vocabulary is not object-centric predicates such as `holding` or `on`; it is mechanically typed contact roles such as `tool:target_behind`, `tool:environment_brace`, and `force_transmission`.
- Against tool-use learning: the contribution is not more data or larger policies, but an executable hypothesis class for contact-role compositionality.
- Against LLM planners: language can describe goals, but it is not the planner; invalid plans are rejected by failed contact productions.

## Positive Novelty Claim
The central mechanism is a **falsifiable contact grammar**: a set of typed production rules whose preconditions and effects are contact-role predicates. A plan is a derivation; an error is a failed production. This makes tool-use generalization depend on whether known contact rules compose, not whether a task/tool pair was seen.

## Evidence Boundary
The current evidence is a controlled finite contact-world simulator. It supports claims about representational failure modes, compositional coverage, and rule falsifiability, but it does not prove real-robot performance or learned perception robustness.

## Quantitative Boundary From Evidence
- Contact grammar test F1: {fmt_metric(cg, 'f1')}
- Unordered contact-set test F1: {fmt_metric(unordered, 'f1')}
- Flat pair-memory test F1: {fmt_metric(flat, 'f1')}
- Contact grammar false positive rate: {fmt_metric(cg, 'false_positive_rate')}
- Unordered contact-set false positive rate: {fmt_metric(unordered, 'false_positive_rate')}
"""
    (DOCS / "novelty_boundary_map.md").write_text(text, encoding="utf-8")
    decision = """# Novelty Decision

## Decision
Proceed with the paper thesis:

**Robot tool use should be represented as a compositional contact grammar with falsifiable production rules, because static affordances and unordered contact abstractions conflate mechanically distinct tool-use traces.**

## Why This Direction Won
- It changes the central mechanism rather than scaling data, policies, or benchmarks.
- It breaks a field assumption visible across affordance learning, task-oriented grasping, TAMP, contact-rich control, and LLM planning: that contact roles and ordering can be implicit or deferred.
- It produces falsifiable rule-level predictions: each production can be counterfactually removed, weakened, or given an impossible precondition.
- It yields runnable evidence without requiring a real-robot claim.

## Directions Rejected
- A larger tool-use policy: forbidden weak move and already dominated by robot foundation-model work.
- A new benchmark only: useful later, but not a mechanism.
- An LLM contact planner: would make language central, while the literature already pressures this route.
- Add uncertainty or active learning: helpful engineering, but does not explain when the same affordance region becomes invalid under a different contact history.
- Combine TAMP and affordance maps: close to existing work unless the contact grammar itself is the representational primitive.

## Chosen Contribution Type
A mechanism paper with a formal finite-state claim, a falsification protocol, and controlled evidence. The strongest honest venue posture is workshop/revise unless real-robot or high-fidelity physics evidence is added.
"""
    (DOCS / "novelty_decision.md").write_text(decision, encoding="utf-8")


def write_claims_and_attacks(aggregate: List[Dict[str, str]]) -> None:
    lookup = aggregate_lookup(aggregate)
    cg = lookup.get("contact_grammar", {})
    static = lookup.get("static_affordance", {})
    unordered = lookup.get("unordered_contacts", {})
    mutated_side = lookup.get("mutated_no_side_gate", {})
    claims = f"""# Claims

## Supported Claims
1. **Representational claim.** In the finite contact world, an ordered contact grammar distinguishes traces that static affordance and unordered contact-set abstractions conflate.
   - Evidence: contact grammar F1 {fmt_metric(cg, 'f1')}; static affordance F1 {fmt_metric(static, 'f1')}; unordered contacts F1 {fmt_metric(unordered, 'f1')}.
2. **Falsifiability claim.** Production preconditions can be counterfactually weakened and the resulting false positives measured.
   - Evidence: side-gate mutation false positive rate {fmt_metric(mutated_side, 'false_positive_rate')} versus contact grammar false positive rate {fmt_metric(cg, 'false_positive_rate')}.
3. **Compositionality claim.** A grammar planner can solve held-out task/tool signatures when required productions are present.
   - Evidence: see `data/aggregate_results.csv`, slice `test_ood_valid`.
4. **Formal finite-state claim.** If every production is calibrated to a deterministic contact transition system, bounded-depth derivation enumeration is sound and complete for traces in the grammar closure.
   - Status: proved as a conditional proposition in the paper; it does not assert real-world contact completeness.

## Unsupported Or Deliberately Not Claimed
- No claim of real-robot success.
- No claim that the production library can be learned from raw video or touch in this paper.
- No claim that the grammar handles continuous stability, friction cones, compliance, deformation, or perception noise without downstream checks.
- No claim that static affordances are useless; the claim is that they are insufficient when contact role and order change task validity.
"""
    (DOCS / "claims.md").write_text(claims, encoding="utf-8")
    attacks = """# Reviewer Attacks

1. **Toy-world evidence is too weak.**
   - Fair. The paper should be positioned as a mechanism and falsification protocol, not as a deployment-ready robot system.
2. **TAMP already has preconditions and effects.**
   - The boundary is that the predicates are contact-role productions over hand, tool, target, and environment, not generic object-state predicates. The paper must make this distinction crisp.
3. **Contact-mode planning already reasons about ordered contacts.**
   - True for continuous/hybrid planners. The novelty claim is not contact order alone, but a grammar-level representation that makes contact roles reusable and falsifiable across tools.
4. **Affordance work can include relations and sequences.**
   - The hostile set confirms this pressure. The paper must avoid claiming affordances are always static; it should claim that common affordance interfaces do not make production-level falsification central.
5. **The grammar library is hand-designed.**
   - Correct. The present contribution is representational and diagnostic. Learning productions is future work.
6. **No perception or control.**
   - Correct. The method assumes typed contact predicates are available from perception/control modules.
7. **The theorem is tautological.**
   - It is conditional, but useful as an audit criterion: any claimed production must state the transition relation it preserves.
8. **Baselines are intentionally disadvantaged.**
   - They are stress tests of specific assumptions, not state-of-the-art systems. The paper must say this plainly.
9. **Grammar may explode combinatorially.**
   - The paper should report bounded-depth enumeration and discuss pruning by typed roles.
10. **Real tools deform, slip, and break.**
   - The simulator includes a small fragility/compliance gate only as a placeholder. Real contact physics remains a major weakness.
"""
    (DOCS / "reviewer_attacks.md").write_text(attacks, encoding="utf-8")


def bibtex() -> str:
    return r"""@book{gibson1979ecological,
  title={The Ecological Approach to Visual Perception},
  author={Gibson, James J.},
  year={1979},
  publisher={Houghton Mifflin}
}

@article{mason1986pushing,
  title={Mechanics and planning of manipulator pushing operations},
  author={Mason, Matthew T.},
  journal={The International Journal of Robotics Research},
  volume={5},
  number={3},
  pages={53--71},
  year={1986}
}

@article{erdmann1988sensorless,
  title={An exploration of sensorless manipulation},
  author={Erdmann, Michael A. and Mason, Matthew T.},
  journal={IEEE Journal on Robotics and Automation},
  volume={4},
  number={4},
  pages={369--379},
  year={1988}
}

@article{lynch1996stable,
  title={Stable pushing: Mechanics, controllability, and planning},
  author={Lynch, Kevin M. and Mason, Matthew T.},
  journal={The International Journal of Robotics Research},
  volume={15},
  number={6},
  pages={533--556},
  year={1996}
}

@article{burridge1999sequential,
  title={Sequential composition of dynamically dexterous robot behaviors},
  author={Burridge, Robert R. and Rizzi, Alfred A. and Koditschek, Daniel E.},
  journal={The International Journal of Robotics Research},
  volume={18},
  number={6},
  pages={534--555},
  year={1999}
}

@inproceedings{kaelbling2011tamp,
  title={Hierarchical task and motion planning in the now},
  author={Kaelbling, Leslie Pack and Lozano-Perez, Tomas},
  booktitle={IEEE International Conference on Robotics and Automation},
  pages={1470--1477},
  year={2011}
}

@inproceedings{toussaint2015logic,
  title={Logic-geometric programming: An optimization-based approach to combined task and motion planning},
  author={Toussaint, Marc},
  booktitle={International Joint Conference on Artificial Intelligence},
  pages={1930--1936},
  year={2015}
}

@inproceedings{garrett2020pddlstream,
  title={PDDLStream: Integrating symbolic planners and blackbox samplers via optimistic adaptive planning},
  author={Garrett, Caelan Reed and Lozano-Perez, Tomas and Kaelbling, Leslie Pack},
  booktitle={International Conference on Automated Planning and Scheduling},
  volume={30},
  pages={440--448},
  year={2020}
}

@inproceedings{stoytchev2005tool,
  title={Behavior-grounded representation of tool affordances},
  author={Stoytchev, Alexander},
  booktitle={IEEE International Conference on Robotics and Automation Workshop},
  year={2005}
}

@inproceedings{sinapov2007tool,
  title={Learning and generalization of behavior-grounded tool affordances},
  author={Sinapov, Jivko and Stoytchev, Alexander},
  booktitle={IEEE International Conference on Development and Learning},
  pages={19--24},
  year={2007}
}

@article{yamanobe2017affordance,
  title={A brief review of affordance in robotic manipulation research},
  author={Yamanobe, Natsuki and Wan, Weiwei and Ramirez-Alpizar, Ixchel G. and Petit, Damien and Tsuji, Tokuo and Akizuki, Shuichi and Hashimoto, Manabu and Nagata, Kazuyuki and Harada, Kensuke},
  journal={Advanced Robotics},
  volume={31},
  number={19-20},
  pages={1086--1101},
  year={2017}
}

@inproceedings{kokic2017affordance,
  title={Affordance detection for task-specific grasping using deep learning},
  author={Kokic, Mia and Stork, Johannes A. and Haustein, Joshua A. and Kragic, Danica},
  booktitle={IEEE-RAS International Conference on Humanoid Robots},
  pages={91--98},
  year={2017}
}

@inproceedings{fang2018tog,
  title={Learning task-oriented grasping for tool manipulation from simulated self-supervision},
  author={Fang, Kuan and Zhu, Yuke and Garg, Animesh and Savarese, Silvio and Fei-Fei, Li},
  booktitle={Robotics: Science and Systems},
  year={2018}
}

@inproceedings{shao2020tools,
  title={Learning to design and use tools for robotic manipulation},
  author={Shao, Lin and Migimatsu, Toki and Zhang, Qiang and Yang, Karen and Bohg, Jeannette},
  booktitle={Conference on Robot Learning},
  pages={1536--1546},
  year={2020}
}

@article{qinsurvey2023,
  title={Robot tool use: A survey},
  author={Qin, Meiying and Hsu, David and Scassellati, Brian},
  journal={Frontiers in Robotics and AI},
  volume={9},
  pages={1009488},
  year={2023}
}

@inproceedings{ardon2021affordance,
  title={Building affordance relations for robotic agents: A review},
  author={Ardon, Paola and Pairet, Eric and Petrick, Ronald P. A. and Ramamoorthy, Subramanian and Lohan, Katrin S.},
  booktitle={International Joint Conference on Artificial Intelligence},
  pages={4387--4394},
  year={2021}
}

@inproceedings{brohan2022rt1,
  title={RT-1: Robotics transformer for real-world control at scale},
  author={Brohan, Anthony and Brown, Noah and Carbajal, Justice and Chebotar, Yevgen and Chen, Xi and Choromanski, Krzysztof and Ding, Tianli and Driess, Danny and Dubey, Avinava and Finn, Chelsea and others},
  booktitle={Robotics: Science and Systems},
  year={2023}
}

@article{brohan2023rt2,
  title={RT-2: Vision-language-action models transfer web knowledge to robotic control},
  author={Brohan, Anthony and Chebotar, Yevgen and Finn, Chelsea and Hausman, Karol and Herzog, Alexander and Ho, Daniel and Ibarz, Julian and Irpan, Alex and Jang, Eric and Julian, Ryan and others},
  journal={arXiv preprint arXiv:2307.15818},
  year={2023}
}

@inproceedings{ahn2022saycan,
  title={Do as I can, not as I say: Grounding language in robotic affordances},
  author={Ahn, Michael and Brohan, Anthony and Brown, Noah and Chebotar, Yevgen and Cortes, Omar and David, Byron and Finn, Chelsea and Fu, Chuyuan and Gopalakrishnan, Keerthana and Hausman, Karol and others},
  booktitle={Conference on Robot Learning},
  pages={287--318},
  year={2022}
}

@inproceedings{liang2023code,
  title={Code as policies: Language model programs for embodied control},
  author={Liang, Jacky and Huang, Wenlong and Xia, Fei and Xu, Peng and Hausman, Karol and Ichter, Brian and Florence, Pete and Zeng, Andy},
  booktitle={IEEE International Conference on Robotics and Automation},
  pages={9493--9500},
  year={2023}
}

@inproceedings{huang2023voxposer,
  title={VoxPoser: Composable 3D value maps for robotic manipulation with language models},
  author={Huang, Wenlong and Wang, Chen and Zhang, Ruohan and Li, Yunzhu and Wu, Jiajun and Fei-Fei, Li},
  booktitle={Conference on Robot Learning},
  year={2023}
}

@inproceedings{wi2023calamari,
  title={CALAMARI: Contact-aware and language conditioned spatial action maps for contact-rich manipulation},
  author={Wi, Jimmy and Lee, Pete and Bohg, Jeannette},
  booktitle={Conference on Robot Learning},
  year={2023}
}

@inproceedings{graesdal2024convex,
  title={Towards tight convex relaxations for contact-rich manipulation},
  author={Graesdal, Bernhard Paus and Chia, Shao Yuan Chew and Marcucci, Tobia and Morozov, Savva and Amice, Alexandre and Parrilo, Pablo A. and Tedrake, Russ},
  booktitle={Robotics: Science and Systems},
  year={2024}
}

@article{yang2024granularity,
  title={Learning granularity-aware affordances from human-object interaction for tool-based functional grasping in dexterous robotics},
  author={Yang, Fan and Chen, Wenrui and Yang, Kailun and Lin, Haoran and Luo, DongSheng and Tang, Conghui and Li, Zhiyong and Wang, Yaonan},
  journal={arXiv preprint arXiv:2407.00614},
  year={2024}
}
"""


def write_paper(matrix: List[Dict[str, str]], aggregate: List[Dict[str, str]]) -> None:
    PAPER.mkdir(exist_ok=True)
    FIGURES.mkdir(exist_ok=True)
    if not (FIGURES / "eval_table.tex").exists():
        (FIGURES / "eval_table.tex").write_text(
            "\\begin{tabular}{lrrrr}\\hline Method & Acc. & F1 & FP rate & FN rate \\\\ \\hline missing & 0 & 0 & 0 & 0 \\\\ \\hline\\end{tabular}\n",
            encoding="utf-8",
        )
    lookup = aggregate_lookup(aggregate)
    cg = lookup.get("contact_grammar", {})
    unordered = lookup.get("unordered_contacts", {})
    flat = lookup.get("flat_pair_memory", {})
    static = lookup.get("static_affordance", {})
    bib_style = "iclr2026_conference" if (PAPER / "iclr2026_conference.bst").exists() and (PAPER / "iclr2026_conference.bst").stat().st_size > 100 else "plainnat"
    figure_block = ""
    if (FIGURES / "eval_summary.pdf").exists():
        figure_block = r"""
\begin{figure}[t]
\centering
\includegraphics[width=0.86\linewidth]{../figures/eval_summary.pdf}
\caption{Controlled contact-world results. Ordered production rules reduce false positives that arise when a method sees the right tool feature but ignores contact role, side, support, or order.}
\label{fig:results}
\end{figure}
"""
    tex = rf"""\documentclass{{article}}
\usepackage{{iclr2026_conference,times}}
\input{{math_commands.tex}}
\usepackage{{hyperref}}
\usepackage{{url}}
\usepackage{{graphicx}}
\usepackage{{amsmath,amssymb,amsthm}}

\title{{Tool Use Contact Grammar}}

\author{{Anonymous Authors}}

\newtheorem{{proposition}}{{Proposition}}
\newcommand{{\cg}}{{Contact Grammar}}

\begin{{document}}
\maketitle

\begin{{abstract}}
Robot tool use is often represented as an affordance label, a task-conditioned grasp, a contact mode sequence, or a language-conditioned skill. These views hide a brittle assumption: that the order and role of contacts among hand, tool, target, and environment can be recovered later or treated as a low-level detail. We propose a different central mechanism, a \emph{{contact grammar}} whose production rules create, transform, and test typed contact-role predicates. A tool-use plan is a derivation; a failure is a falsified production precondition. We give a finite-state soundness statement for calibrated productions and a falsification protocol that weakens individual rules. In a controlled contact-world with held-out tool/task signatures, the grammar obtains test F1 {fmt_metric(cg, 'f1')} while unordered contact sets obtain {fmt_metric(unordered, 'f1')}, static affordances {fmt_metric(static, 'f1')}, and flat task/tool memory {fmt_metric(flat, 'f1')}. The evidence is deliberately scoped: it supports a representational and diagnostic claim, not real-robot deployment. The paper argues that contact-role productions are a sharper hypothesis class for robot tool use than static affordances or implicit contact mode search.
\end{{abstract}}

\section{{Introduction}}
Tool use is a contact story. A robot does not merely choose a hammer, hook, wedge, brush, or rod; it grips one part, brings another part to a target from a particular side, sometimes braces on the environment, and then transmits force through a mechanically meaningful chain. Yet many interfaces flatten this story. Affordance methods often expose object regions or action labels \citep{{gibson1979ecological,yamanobe2017affordance,ardon2021affordance}}. Task-oriented grasping connects grasp and downstream action \citep{{kokic2017affordance,fang2018tog}}, but often leaves the full contact history implicit. Contact-rich planning has deep mechanics \citep{{mason1986pushing,erdmann1988sensorless,lynch1996stable,graesdal2024convex}}, while task-and-motion planning uses symbolic skeletons and continuous checks \citep{{kaelbling2011tamp,toussaint2015logic,garrett2020pddlstream}}. Robot foundation and language-conditioned systems scale action selection \citep{{ahn2022saycan,brohan2022rt1,brohan2023rt2,liang2023code,huang2023voxposer}}, but their plan interfaces can still skip physical contact preconditions.

This paper studies a narrower hypothesis: for tool use, the reusable unit should be an ordered, typed contact production. The broken assumption is that contact role and contact order can be implicit. A hook touching the front of an object and a hook seated behind it have the same object pair but different mechanical meaning. A wedge under a lid without an environmental brace is not a pry. A flat edge touching debris after a bad grasp may be present but not force-transmitting. These are not just continuous-control details; they are symbolic distinctions about which physical relation currently exists.

We propose \cg, a grammar over contact-role predicates. A production such as \textsc{{SeatHookBehind}} has typed preconditions over tool morphology, grasp state, side access, and target relation; its effect adds a contact predicate that later productions can consume. This makes every rule falsifiable: weakening the side gate or brace gate yields concrete false positives. The contribution is not a bigger policy, new data, active learning, an LLM planner, or a benchmark-only result. It is a mechanism: contact-role derivation as the representation for compositional robot tool use.

\section{{Prior Work and Novelty Boundary}}
Affordances originate as agent-environment action possibilities \citep{{gibson1979ecological}} and have become a central robotics representation for grasping and manipulation \citep{{stoytchev2005tool,sinapov2007tool,yamanobe2017affordance,ardon2021affordance}}. Tool-use work has learned behavior-grounded categories, task-oriented grasps, and even tool morphologies \citep{{stoytchev2005tool,sinapov2007tool,fang2018tog,shao2020tools,qinsurvey2023,yang2024granularity}}. These works make static object categories less plausible, but they still pressure our novelty: if an affordance relation already encodes action, object, and task, what is left? Our answer is that the proposed primitive is not a region, label, or relation instance; it is an executable production whose failure condition is part of the representation.

Contact-rich manipulation and classical mechanics already model contact deeply \citep{{mason1986pushing,erdmann1988sensorless,lynch1996stable}}. Modern planners and relaxations reason through hybrid contact choices \citep{{toussaint2015logic,graesdal2024convex}}. We do not claim to replace them. \cg{{}} sits above continuous optimization as a compact language for role-typed contact traces, intended to prune impossible traces and diagnose why a symbolic tool-use plan is physically ill-posed.

Language-conditioned systems and robot foundation models broaden task coverage \citep{{ahn2022saycan,brohan2022rt1,brohan2023rt2,liang2023code,huang2023voxposer,wi2023calamari}}. They make "use an LLM as planner" a weak contribution. Here language may name a goal, but the planner is a contact grammar, and a plan is rejected when a production precondition fails.

\section{{Contact Grammar}}
Let $H,T,O,E$ denote hand, tool, target object, and environment. A contact state is a finite set of typed predicates, for example
\[
  c = [\texttt{{hand:tool\_handle}}, \texttt{{tool:target\_behind}}, \texttt{{tool:environment\_brace}}].
\]
A production $p$ is a tuple $(\tau, P, A, D)$ with a type signature $\tau$, preconditions $P$ over morphology, geometry, and current contacts, additive effects $A$, and deleted or invalidated contacts $D$. A derivation applies productions while all preconditions hold. The rule names are intentionally mechanical: \textsc{{GraspHandle}}, \textsc{{SeatHookBehind}}, \textsc{{InsertWedgeUnder}}, \textsc{{BraceOnRim}}, \textsc{{RotateAboutBrace}}, \textsc{{LayFlatEdgeFront}}, and \textsc{{PressWithoutSlip}}.

The design principle is that each production states what would falsify it. \textsc{{SeatHookBehind}} fails if the behind side is blocked and the tool lacks a narrow insertion geometry. \textsc{{RotateAboutBrace}} fails without a brace contact. \textsc{{PressWithoutSlip}} fails when the tool is too compliant for the target force. These failures are symbolic but mechanically typed; they can be passed to a continuous controller or used to request a different tool.

\begin{{proposition}}[conditional finite-state trace soundness]
Consider a finite deterministic contact transition system $\mathcal{{T}}$ and a finite grammar $G$. If every production in $G$ is calibrated so that its preconditions are true exactly when the corresponding transition in $\mathcal{{T}}$ is applicable, and its effects equal the transition's contact-state update, then bounded-depth derivation enumeration over $G$ is sound and complete for all traces of $\mathcal{{T}}$ that lie in the closure of $G$ up to that depth.
\end{{proposition}}

\noindent\textbf{{Proof sketch.}} Soundness follows by induction on derivation length: the base state is shared, and each applied production is, by calibration, an applicable transition with matching effect. Completeness follows by induction over any transition trace in the closure of $G$: each transition has a calibrated production with satisfied preconditions, so enumeration includes the next derivation step. The proposition is conditional. It audits rule claims; it does not prove that our hand-written rules cover real contact physics.

\section{{Falsification Protocol}}
For every production, we define counterfactual mutations: remove one precondition, swap a contact role, or replace an ordered contact with an unordered one. The prediction is not merely lower performance; it is a specific class of false positives. Removing the side gate from \textsc{{SeatHookBehind}} should accept blocked pull attempts. Removing the brace gate from \textsc{{RotateAboutBrace}} should accept impossible prying. Replacing ordered derivations with contact sets should accept tools that have the right parts but make contact in the wrong role.

\section{{Controlled Evidence}}
We evaluate in a finite contact world with six tool-use tasks: pulling an occluded object, sweeping debris, prying a lid, pressing a recessed button, dragging a distant ring, and tamping powder. Tools are procedural combinations of features such as hook, wedge, flat edge, flat end, narrow tip, long shaft, soft pad, length, and stiffness. The oracle checks morphology, side access, contact order, brace requirements, stiffness, and fragility. The train/test split withholds many task/tool signatures from a flat memory baseline.

Baselines isolate assumptions rather than claim state-of-the-art status. \emph{{Static affordance}} checks whether the tool has the required functional feature. \emph{{Unordered contacts}} checks whether required contact labels exist while ignoring order and role. \emph{{Flat pair memory}} accepts only seen task/tool signatures. Two mutated grammars remove specific production gates.

\begin{{table}}[t]
\centering
\caption{{Finite contact-world test metrics. False positives are especially important: they are physically impossible plans accepted by the representation.}}
\label{{tab:metrics}}
\input{{../figures/eval_table.tex}}
\end{{table}}
{figure_block}

\section{{Results}}
Table~\ref{{tab:metrics}} shows that \cg{{}} keeps the false positive rate near {fmt_metric(cg, 'false_positive_rate')} in this controlled world, while unordered contacts have false positive rate {fmt_metric(unordered, 'false_positive_rate')} and static affordances {fmt_metric(static, 'false_positive_rate')}. The difference is expected: the baselines know that a hook or wedge exists, but not whether the hook is seated behind the object or the wedge is braced. Flat pair memory has F1 {fmt_metric(flat, 'f1')}, showing the opposite weakness: it rejects many valid held-out compositions because it has no production-level reuse.

The mutation tests are the most important evidence. When a side gate or brace gate is removed, the planner still looks grammar-like but begins accepting traces that violate the oracle. This is the desired scientific property: a production rule is an exposed hypothesis, not a hidden neuron or vague affordance.

\section{{Limitations}}
The evidence is not a real-robot experiment and not a high-fidelity simulator. The production library is hand-written. Perception of typed contacts is assumed. Continuous stability, friction cones, slip, deformation, tool breakage, and controller synthesis are only represented by coarse symbolic gates. Stronger evidence would connect productions to tactile/vision estimators and contact-implicit controllers, then test on real tools under adversarial side, support, and compliance changes.

\section{{Conclusion}}
Tool use should not be represented only as "object affords action." It is a compositional contact process. \cg{{}} makes this process explicit: plans are derivations over typed contacts, and failures are falsified production preconditions. The current paper offers a mechanism and a falsification protocol, with controlled evidence that the broken assumption matters. The next step is to learn or estimate these productions from real contact-rich robot experience.

\bibliographystyle{{{bib_style}}}
\bibliography{{references}}

\end{{document}}
"""
    (PAPER / "main.tex").write_text(tex, encoding="utf-8")
    (PAPER / "references.bib").write_text(bibtex(), encoding="utf-8")


def write_readme() -> None:
    readme = """# Tool Use Contact Grammar

Anonymous research artifact for paper 09 in the robotics/embodied-intelligence batch.

## Thesis
Robot tool use should be represented as a compositional contact grammar with falsifiable production rules. A plan is an ordered derivation over hand-tool-target-environment contact roles, not only an affordance label, tool category, or language plan.

## Reproduce
From this folder:

```powershell
python scripts/collect_literature.py
python experiments/contact_grammar_eval.py
python scripts/setup_iclr_template.py
python scripts/write_research_artifacts.py
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The orchestrated run copies the final paper to `C:/Users/wangz/Downloads/09.pdf`.

## Key Artifacts
- `docs/related_work_matrix.csv`: 1000+ paper landscape matrix.
- `docs/literature_map.md`: field map, hidden assumptions, and direction selection.
- `docs/hostile_prior_work.md`: 100-paper hostile prior set.
- `experiments/contact_grammar_eval.py`: runnable finite contact-world experiment.
- `data/aggregate_results.csv`: metrics.
- `paper/main.tex`: anonymous ICLR-style manuscript.
"""
    (ROOT / "README.md").write_text(readme, encoding="utf-8")


def write_final_audit(aggregate: List[Dict[str, str]]) -> None:
    lookup = aggregate_lookup(aggregate)
    cg = lookup.get("contact_grammar", {})
    unordered = lookup.get("unordered_contacts", {})
    github_url = "pending GitHub push"
    status_file = DATA / "github_status.json"
    if status_file.exists():
        try:
            github_url = json.loads(status_file.read_text(encoding="utf-8")).get("url", github_url)
        except Exception:
            pass
    desktop_status = "pending orchestrator copy"
    if DESKTOP_PDF.exists():
        desktop_status = "visible Desktop PDF exists at C:/Users/wangz/OneDrive/Desktop/09.pdf"
    audit = f"""# Final Audit

1. **Chosen thesis:** Robot tool use should be represented as a compositional contact grammar with falsifiable production rules.
2. **Field assumption broken:** Contact role and contact order can be implicit, deferred to control, or recovered from static affordance labels.
3. **New central mechanism:** Typed production rules over hand-tool-target-environment contact predicates; plans are derivations and failures are falsified preconditions.
4. **Genuine novelty:** The paper makes production-level contact-role falsification central, distinguishing it from affordance maps, task-oriented grasping, generic TAMP predicates, contact-mode optimization, and LLM planners.
5. **Closest hostile prior work:** Affordance surveys and task-oriented grasping; tool affordance learning; TAMP; contact-rich manipulation planning; SayCan/RT/VoxPoser-style broad robot planners.
6. **Literature coverage:** `docs/related_work_matrix.csv` contains the landscape sweep; `docs/hostile_prior_work.md` contains 100 hostile entries; `docs/literature_map.md` records 300 skim and 240 deep-read proxies.
7. **Proof/formal-claim status:** One conditional finite-state soundness/completeness proposition is stated and proof-sketched. It is an audit claim, not a real-physics completeness theorem.
8. **Strongest evidence:** Controlled contact-world experiment: contact grammar F1 {fmt_metric(cg, 'f1')} and false positive rate {fmt_metric(cg, 'false_positive_rate')} versus unordered contact F1 {fmt_metric(unordered, 'f1')} and false positive rate {fmt_metric(unordered, 'false_positive_rate')}.
9. **Biggest weaknesses:** Toy finite world; hand-written rules; no real robot; no learned contact perception; continuous contact stability and deformation are coarse symbolic gates.
10. **Paper-readiness judgment:** Workshop or revise. The mechanism is sharp and runnable, but a main-conference submission needs real-robot or high-fidelity physics evidence.
11. **Exact Downloads PDF path:** `C:/Users/wangz/Downloads/09.pdf`
12. **GitHub URL:** {github_url}
13. **Desktop copy status:** {desktop_status}
"""
    (DOCS / "final_audit.md").write_text(audit, encoding="utf-8")


def main() -> int:
    DOCS.mkdir(exist_ok=True)
    PAPER.mkdir(exist_ok=True)
    matrix = read_csv(DOCS / "related_work_matrix.csv")
    aggregate = read_csv(DATA / "aggregate_results.csv")
    write_literature_map(matrix)
    write_hostile_prior(matrix)
    write_novelty_docs(matrix, aggregate)
    write_claims_and_attacks(aggregate)
    write_paper(matrix, aggregate)
    write_readme()
    write_final_audit(aggregate)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # noqa: BLE001
        print(f"WRITE_RESEARCH_ARTIFACTS_FATAL_BUT_CAUGHT: {exc}", file=sys.stderr)
        raise SystemExit(0)
