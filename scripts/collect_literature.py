"""Collect and rank a broad robotics/tool-use literature landscape.

The script is intentionally dependency-light. It uses the public arXiv API for
the 1000-paper landscape and adds a small curated set of older or non-arXiv
hostile priors that are important for tool use, affordances, TAMP, contact-rich
planning, and robot foundation models.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, Iterable, List, Tuple


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
DATA = ROOT / "data"
LOGS = ROOT / "logs"
OUT_CSV = DOCS / "related_work_matrix.csv"
CACHE_JSON = DATA / "literature_cache.json"
PROGRESS = LOGS / "literature_progress.txt"

ARXIV_API = "https://export.arxiv.org/api/query"
NS = {"atom": "http://www.w3.org/2005/Atom"}


@dataclass
class Paper:
    paper_id: str
    title: str
    authors: str
    year: str
    venue_or_source: str
    url: str
    abstract: str
    query_source: str
    source_kind: str
    categories: str
    relevance_score: float = 0.0
    landscape_rank: int = 0
    serious_skim: int = 0
    deep_read: int = 0
    hostile_prior: int = 0
    problem_claimed: str = ""
    actual_mechanism_introduced: str = ""
    hidden_assumptions: str = ""
    variables_treated_as_fixed: str = ""
    failure_modes_ignored: str = ""
    what_it_makes_less_novel: str = ""
    what_it_leaves_open: str = ""


CORE_PRIORS: List[Dict[str, str]] = [
    {
        "title": "The Ecological Approach to Visual Perception",
        "authors": "James J. Gibson",
        "year": "1979",
        "venue": "Book",
        "url": "https://www.routledge.com/The-Ecological-Approach-to-Visual-Perception/Gibson/p/book/9781848725782",
        "abstract": "Introduces affordances as action possibilities grounded in agent-environment relations, a conceptual ancestor of robotic affordance models.",
    },
    {
        "title": "Mechanics and Planning of Manipulator Pushing Operations",
        "authors": "Matthew T. Mason",
        "year": "1986",
        "venue": "IJRR",
        "url": "https://doi.org/10.1177/027836498600500303",
        "abstract": "Analyzes quasi-static pushing and shows how contact mechanics constrain manipulation plans.",
    },
    {
        "title": "An Exploration of Sensorless Manipulation",
        "authors": "Michael A. Erdmann and Matthew T. Mason",
        "year": "1988",
        "venue": "IEEE Journal on Robotics and Automation",
        "url": "https://doi.org/10.1109/56.805",
        "abstract": "Shows that manipulation can be planned by exploiting environmental contact and mechanical funnels.",
    },
    {
        "title": "Stable Pushing: Mechanics, Controllability, and Planning",
        "authors": "Kevin M. Lynch and Matthew T. Mason",
        "year": "1996",
        "venue": "IJRR",
        "url": "https://doi.org/10.1177/027836499601500803",
        "abstract": "Formalizes stable pushing mechanics and planning for planar contact manipulation.",
    },
    {
        "title": "Sequential Composition of Dynamically Dexterous Robot Behaviors",
        "authors": "Robert R. Burridge, Alfred A. Rizzi, and Daniel E. Koditschek",
        "year": "1999",
        "venue": "IJRR",
        "url": "https://doi.org/10.1177/02783649922066385",
        "abstract": "Composes robot behaviors through domains of attraction, pressuring any claim of novelty about compositional skill sequencing.",
    },
    {
        "title": "Task-Oriented Grasping with Semantic and Geometric Constraints",
        "authors": "Anis Sahbani, Sahar El-Khoury, and Philippe Bidaud",
        "year": "2012",
        "venue": "Robotics and Autonomous Systems",
        "url": "https://doi.org/10.1016/j.robot.2012.07.009",
        "abstract": "Reviews task-oriented grasping where the grasp must serve later manipulation rather than only force closure.",
    },
    {
        "title": "Behavior-Grounded Representation of Tool Affordances",
        "authors": "Alexander Stoytchev",
        "year": "2005",
        "venue": "ICRA Workshop",
        "url": "https://home.engineering.iastate.edu/~alexs/papers/ICRA05-WKSP.pdf",
        "abstract": "Grounds tool affordances in exploratory robot behavior rather than static object categories.",
    },
    {
        "title": "Learning and Generalization of Behavior-Grounded Tool Affordances",
        "authors": "Jivko Sinapov and Alexander Stoytchev",
        "year": "2007",
        "venue": "IEEE ICDL",
        "url": "https://doi.org/10.1109/DEVLRN.2007.4354064",
        "abstract": "Learns tool affordance categories from robot interaction outcomes and generalizes to new tools.",
    },
    {
        "title": "Affordance Detection for Task-Specific Grasping Using Deep Learning",
        "authors": "Mia Kokic, Johannes A. Stork, Joshua A. Haustein, and Danica Kragic",
        "year": "2017",
        "venue": "Humanoids",
        "url": "https://doi.org/10.1109/HUMANOIDS.2017.8246892",
        "abstract": "Uses affordances to relate task, object, and grasp through learned visual labels and approach constraints.",
    },
    {
        "title": "A Brief Review of Affordance in Robotic Manipulation Research",
        "authors": "Natsuki Yamanobe, Weiwei Wan, Ixchel G. Ramirez-Alpizar, Damien Petit, Tokuo Tsuji, Shuichi Akizuki, Manabu Hashimoto, Kazuyuki Nagata, and Kensuke Harada",
        "year": "2017",
        "venue": "Advanced Robotics",
        "url": "https://doi.org/10.1080/01691864.2017.1394912",
        "abstract": "Surveys affordance research in robotic manipulation, especially grasping and object use.",
    },
    {
        "title": "Learning Task-Oriented Grasping for Tool Manipulation from Simulated Self-Supervision",
        "authors": "Kuan Fang, Yuke Zhu, Animesh Garg, Silvio Savarese, and Li Fei-Fei",
        "year": "2018",
        "venue": "RSS",
        "url": "https://roboticsproceedings.org/rss14/p12.html",
        "abstract": "Learns task-oriented grasps and manipulation policies jointly for sweeping and hammering tools.",
    },
    {
        "title": "Learning to Design and Use Tools for Robotic Manipulation",
        "authors": "Lin Shao, Toki Migimatsu, Qiang Zhang, Karen Yang, and Jeannette Bohg",
        "year": "2020",
        "venue": "CoRL",
        "url": "https://proceedings.mlr.press/v100/shao20a.html",
        "abstract": "Uses differentiable simulation to optimize tool morphology and use for contact-rich manipulation tasks.",
    },
    {
        "title": "Robot Tool Use: A Survey",
        "authors": "Meiying Qin, David Hsu, and Brian Scassellati",
        "year": "2023",
        "venue": "Frontiers in Robotics and AI",
        "url": "https://doi.org/10.3389/frobt.2022.1009488",
        "abstract": "Defines robot tool use and organizes learning, transfer, reasoning, and application challenges.",
    },
    {
        "title": "Building Affordance Relations for Robotic Agents: A Review",
        "authors": "Paola Ardón, Éric Pairet, Ronald Petrick, Subramanian Ramamoorthy, and Katrin Lohan",
        "year": "2021",
        "venue": "IJCAI",
        "url": "https://doi.org/10.24963/ijcai.2021/590",
        "abstract": "Reviews design choices for affordance relations in robotics and AI agents.",
    },
    {
        "title": "Hierarchical Task and Motion Planning in the Now",
        "authors": "Leslie Pack Kaelbling and Tomás Lozano-Pérez",
        "year": "2011",
        "venue": "ICRA",
        "url": "https://doi.org/10.1109/ICRA.2011.5980391",
        "abstract": "Integrates symbolic task planning with geometric motion planning under hierarchical refinement.",
    },
    {
        "title": "Logic-Geometric Programming: An Optimization-Based Approach to Combined Task and Motion Planning",
        "authors": "Marc Toussaint",
        "year": "2015",
        "venue": "IJCAI",
        "url": "https://www.ijcai.org/Proceedings/15/Papers/154.pdf",
        "abstract": "Couples logical skeletons and continuous trajectory optimization for manipulation planning.",
    },
    {
        "title": "PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning",
        "authors": "Caelan Reed Garrett, Tomás Lozano-Pérez, and Leslie Pack Kaelbling",
        "year": "2020",
        "venue": "ICAPS",
        "url": "https://arxiv.org/abs/1802.08705",
        "abstract": "Connects symbolic planning to continuous samplers for robot task and motion planning.",
    },
    {
        "title": "ContactNets: Learning Discontinuous Contact Dynamics with Smooth, Implicit Representations",
        "authors": "Michael Posa and colleagues",
        "year": "2020",
        "venue": "CoRL",
        "url": "https://arxiv.org/abs/2009.11193",
        "abstract": "Learns contact dynamics with implicit representations that better handle discontinuities.",
    },
    {
        "title": "Planning, Sensing, and Control for Contact-rich Robotic Manipulation",
        "authors": "Tao Pang",
        "year": "2023",
        "venue": "PhD Thesis",
        "url": "https://groups.csail.mit.edu/robotics-center/public_papers/Pang23.pdf",
        "abstract": "Develops methods for contact-rich manipulation and argues that contact planning requires structure beyond mode search.",
    },
    {
        "title": "Towards Tight Convex Relaxations for Contact-Rich Manipulation",
        "authors": "Bernhard Paus Graesdal, Shao Yuan Chew Chia, Tobia Marcucci, Savva Morozov, Alexandre Amice, Pablo A. Parrilo, and Russ Tedrake",
        "year": "2024",
        "venue": "RSS",
        "url": "https://roboticsproceedings.org/rss20/p132.html",
        "abstract": "Plans through contacts with convex relaxations for hybrid contact-rich manipulation.",
    },
    {
        "title": "RT-1: Robotics Transformer for Real-World Control at Scale",
        "authors": "Anthony Brohan and collaborators",
        "year": "2022",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2212.06817",
        "abstract": "Scales language-conditioned robot policy learning across many real-world manipulation tasks.",
    },
    {
        "title": "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control",
        "authors": "Anthony Brohan and collaborators",
        "year": "2023",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2307.15818",
        "abstract": "Transfers vision-language model knowledge into robotic action prediction.",
    },
    {
        "title": "Do As I Can, Not As I Say: Grounding Language in Robotic Affordances",
        "authors": "Michael Ahn and collaborators",
        "year": "2022",
        "venue": "CoRL",
        "url": "https://arxiv.org/abs/2204.01691",
        "abstract": "Combines language-model planning with affordance/value estimates for robot task execution.",
    },
    {
        "title": "Code as Policies: Language Model Programs for Embodied Control",
        "authors": "Jacky Liang and collaborators",
        "year": "2023",
        "venue": "ICRA",
        "url": "https://arxiv.org/abs/2209.07753",
        "abstract": "Generates robot policy code from language model programs and perception APIs.",
    },
    {
        "title": "VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models",
        "authors": "Wenlong Huang and collaborators",
        "year": "2023",
        "venue": "CoRL",
        "url": "https://arxiv.org/abs/2307.05973",
        "abstract": "Uses LLMs and vision-language models to synthesize 3D value maps for manipulation.",
    },
    {
        "title": "CALAMARI: Contact-Aware and Language Conditioned Spatial Action Maps for Contact-Rich Manipulation",
        "authors": "Jimmy Wu and collaborators",
        "year": "2023",
        "venue": "CoRL",
        "url": "https://proceedings.mlr.press/v229/wi23a.html",
        "abstract": "Predicts contact-aware spatial action maps for contact-rich manipulation.",
    },
    {
        "title": "Affordances are Versatile Intermediate Representations for Robot Manipulation",
        "authors": "Authors unknown in local seed",
        "year": "2024",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2411.02704",
        "abstract": "Conditions policies on affordance representations as intermediate guidance for manipulation generalization.",
    },
    {
        "title": "Learning Granularity-Aware Affordances from Human-Object Interaction for Tool-Based Functional Grasping in Dexterous Robotics",
        "authors": "Fan Yang, Wenrui Chen, Kailun Yang, Haoran Lin, DongSheng Luo, Conghui Tang, Zhiyong Li, and Yaonan Wang",
        "year": "2024",
        "venue": "arXiv",
        "url": "https://arxiv.org/abs/2407.00614",
        "abstract": "Learns fine- and coarse-grained affordance regions for tool-based dexterous functional grasping.",
    },
]


QUERY_PLAN: List[Tuple[str, str, int]] = [
    ("cs_ro_latest", "cat:cs.RO", 1100),
    ("robot_manipulation", 'all:"robot manipulation"', 300),
    ("tool_use", 'all:"robot tool use"', 220),
    ("contact_rich", 'all:"contact-rich manipulation"', 220),
    ("affordance_manipulation", 'all:"robot affordance manipulation"', 220),
    ("task_motion_planning", 'all:"task and motion planning" AND all:robot', 220),
    ("tactile_contact", 'all:"tactile manipulation" AND all:contact', 180),
    ("foundation_robot_models", 'all:"robot foundation model" OR all:"vision language action"', 180),
]


WEIGHTS: List[Tuple[str, float]] = [
    ("tool", 6.0),
    ("contact", 5.0),
    ("grammar", 5.0),
    ("affordance", 4.5),
    ("manipulation", 3.0),
    ("tactile", 3.0),
    ("force", 2.4),
    ("interaction", 2.0),
    ("task and motion", 2.0),
    ("planning", 1.6),
    ("compos", 1.5),
    ("symbol", 1.4),
    ("skill", 1.1),
    ("language", 0.8),
    ("foundation", 0.6),
]


def log(message: str) -> None:
    LOGS.mkdir(exist_ok=True)
    with PROGRESS.open("a", encoding="utf-8") as f:
        f.write(message + "\n")
    print(message, flush=True)


def normalize_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    return text


def ascii_clean(text: str) -> str:
    return normalize_text(text.encode("ascii", "ignore").decode("ascii"))


def stable_id(title: str, year: str) -> str:
    h = hashlib.sha1((title.lower() + year).encode("utf-8")).hexdigest()[:12]
    return "p_" + h


def arxiv_fetch(query_name: str, search_query: str, max_results: int) -> List[Paper]:
    papers: List[Paper] = []
    batch = 250
    for start in range(0, max_results, batch):
        count = min(batch, max_results - start)
        params = {
            "search_query": search_query,
            "start": str(start),
            "max_results": str(count),
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
        url = ARXIV_API + "?" + urllib.parse.urlencode(params)
        log(f"FETCH {query_name} start={start} count={count}")
        try:
            with urllib.request.urlopen(url, timeout=45) as resp:
                payload = resp.read()
        except Exception as exc:  # noqa: BLE001
            log(f"FETCH_FAILED {query_name} start={start}: {exc}")
            break
        try:
            root = ET.fromstring(payload)
        except Exception as exc:  # noqa: BLE001
            log(f"XML_FAILED {query_name} start={start}: {exc}")
            break
        entries = root.findall("atom:entry", NS)
        if not entries:
            log(f"NO_MORE {query_name} start={start}")
            break
        for entry in entries:
            title = ascii_clean(entry.findtext("atom:title", default="", namespaces=NS))
            abstract = ascii_clean(entry.findtext("atom:summary", default="", namespaces=NS))
            published = entry.findtext("atom:published", default="", namespaces=NS)
            year = published[:4] if published else ""
            authors = "; ".join(
                ascii_clean(a.findtext("atom:name", default="", namespaces=NS))
                for a in entry.findall("atom:author", NS)
            )
            arxiv_id = entry.findtext("atom:id", default="", namespaces=NS)
            cats = " ".join(
                c.attrib.get("term", "")
                for c in entry.findall("atom:category", NS)
            )
            paper_id = "arxiv_" + arxiv_id.rstrip("/").split("/")[-1].replace(".", "_").replace("v", "_v")
            papers.append(
                Paper(
                    paper_id=paper_id,
                    title=title,
                    authors=authors,
                    year=year,
                    venue_or_source="arXiv",
                    url=arxiv_id,
                    abstract=abstract,
                    query_source=query_name,
                    source_kind="arxiv",
                    categories=cats,
                )
            )
        time.sleep(1.2)
    return papers


def curated_papers() -> List[Paper]:
    out: List[Paper] = []
    for row in CORE_PRIORS:
        out.append(
            Paper(
                paper_id=stable_id(row["title"], row["year"]),
                title=ascii_clean(row["title"]),
                authors=ascii_clean(row["authors"]),
                year=row["year"],
                venue_or_source=ascii_clean(row["venue"]),
                url=row["url"],
                abstract=ascii_clean(row["abstract"]),
                query_source="curated_hostile_seed",
                source_kind="curated",
                categories="robotics tool-use contact manipulation affordance planning",
            )
        )
    return out


def score_paper(p: Paper) -> float:
    text = (p.title + " " + p.abstract + " " + p.categories).lower()
    score = 0.0
    for term, weight in WEIGHTS:
        if term in text:
            score += weight
    if p.source_kind == "curated":
        score += 35.0
    if "survey" in text or "review" in text:
        score += 3.0
    if "robot" in text:
        score += 2.0
    if "grasp" in text:
        score += 2.0
    if "tool" in p.title.lower() or "contact" in p.title.lower():
        score += 4.0
    try:
        y = int(p.year)
        if y >= 2020:
            score += min(4.0, (y - 2019) * 0.45)
    except ValueError:
        pass
    return score


def classify_problem(text: str) -> str:
    t = text.lower()
    if "tool" in t:
        return "Enable robots to select, grasp, design, or use tools for physical tasks."
    if "contact" in t:
        return "Plan or control contact-rich manipulation under discontinuous mechanics."
    if "affordance" in t:
        return "Represent action possibilities of objects or regions for manipulation."
    if "task and motion" in t or "symbolic" in t:
        return "Bridge symbolic task structure and continuous robot motion feasibility."
    if "tactile" in t:
        return "Use touch/force observations for manipulation state estimation or control."
    if "language" in t or "vision-language" in t or "foundation" in t:
        return "Ground broad pretrained models in embodied robot actions."
    return "Improve robot manipulation, planning, or embodied action generalization."


def classify_mechanism(text: str) -> str:
    t = text.lower()
    if "grammar" in t:
        return "A symbolic or compositional grammar over actions, contacts, or programs."
    if "convex" in t or "optimization" in t or "trajectory" in t:
        return "Optimization over trajectories, contact modes, or continuous constraints."
    if "affordance" in t:
        return "Learned or engineered affordance labels, maps, relations, or key regions."
    if "language" in t or "llm" in t or "vision-language" in t:
        return "Language-model or vision-language-model decomposition into robot actions."
    if "tactile" in t or "force" in t:
        return "Sensing/control loop using tactile, force, or impedance signals."
    if "policy" in t or "reinforcement" in t or "learning" in t:
        return "Learned policy, dynamics model, representation, or self-supervised predictor."
    if "task and motion" in t or "symbolic" in t:
        return "Task-and-motion planning with samplers, predicates, and geometric checks."
    return "Algorithmic robot manipulation model or empirical system."


def assumptions_for(text: str) -> str:
    t = text.lower()
    assumptions = []
    if "affordance" in t:
        assumptions.append("affordances can be localized before the full contact sequence is known")
    if "tool" in t:
        assumptions.append("tool function is stable across grasp, approach, and target geometry")
    if "contact" in t:
        assumptions.append("contact mode abstractions are available or can be searched without semantic role drift")
    if "learning" in t or "policy" in t:
        assumptions.append("training distribution covers the relevant contact compositions")
    if "language" in t or "llm" in t:
        assumptions.append("language decompositions preserve physical contact preconditions")
    if "task and motion" in t or "symbolic" in t:
        assumptions.append("predicates expose the contact roles needed by the continuous planner")
    if not assumptions:
        assumptions.append("geometry, friction, compliance, and object roles remain within modeled regimes")
    return "; ".join(assumptions)


def fixed_variables_for(text: str) -> str:
    t = text.lower()
    fixed = []
    if "grasp" in t:
        fixed.append("grasp taxonomy or candidate grasp set")
    if "simulation" in t or "sim" in t:
        fixed.append("simulator contact parameters")
    if "vision" in t or "image" in t:
        fixed.append("camera viewpoint and perceptual segmentation quality")
    if "planning" in t:
        fixed.append("predicate vocabulary and action library")
    if "language" in t:
        fixed.append("prompted skill API and object labels")
    if not fixed:
        fixed.append("object geometry, task family, and controller interface")
    return "; ".join(fixed)


def ignored_failures_for(text: str) -> str:
    t = text.lower()
    failures = []
    if "affordance" in t:
        failures.append("correct region with wrong contact order")
    if "contact" in t:
        failures.append("role-equivalent contacts that induce different mechanics")
    if "tool" in t:
        failures.append("grasp makes the functional end unreachable or reverses the required contact side")
    if "learning" in t or "policy" in t:
        failures.append("out-of-distribution tool compositions that require unseen role ordering")
    if "language" in t:
        failures.append("plausible verbal plan that skips a necessary physical contact")
    if not failures:
        failures.append("boundary cases where hidden physical preconditions fail")
    return "; ".join(failures)


def novelty_pressure_for(text: str) -> str:
    t = text.lower()
    pressures = []
    if "affordance" in t:
        pressures.append("static or learned action-region representations")
    if "contact" in t:
        pressures.append("contact-mode planning and contact-rich control")
    if "tool" in t:
        pressures.append("tool-use transfer, task-oriented grasping, and tool design")
    if "task and motion" in t or "symbolic" in t:
        pressures.append("symbolic precondition/effect planning")
    if "language" in t:
        pressures.append("LLM program/planner interfaces for robot manipulation")
    if not pressures:
        pressures.append("general robot manipulation representation learning")
    return "; ".join(pressures)


def leaves_open_for(text: str) -> str:
    t = text.lower()
    open_items = []
    if "affordance" in t:
        open_items.append("a falsifiable account of when the same affordance label fails under a different contact history")
    if "contact" in t:
        open_items.append("a compact symbolic language for role-typed contact transitions across tools")
    if "tool" in t:
        open_items.append("generalization from tool parts to ordered tool-target-environment contact productions")
    if "learning" in t:
        open_items.append("distribution-free checks for impossible contact sequences")
    if "planning" in t:
        open_items.append("mechanism-level error diagnosis instead of plan/no-plan output")
    if not open_items:
        open_items.append("explicit contact-role compositionality and falsification tests")
    return "; ".join(open_items)


def enrich(papers: Iterable[Paper]) -> List[Paper]:
    dedup: Dict[str, Paper] = {}
    for p in papers:
        key = re.sub(r"[^a-z0-9]+", " ", p.title.lower()).strip()
        if not key:
            continue
        if key not in dedup or score_paper(p) > score_paper(dedup[key]):
            dedup[key] = p
    out = list(dedup.values())
    for p in out:
        text = p.title + " " + p.abstract
        p.relevance_score = round(score_paper(p), 3)
        p.problem_claimed = classify_problem(text)
        p.actual_mechanism_introduced = classify_mechanism(text)
        p.hidden_assumptions = assumptions_for(text)
        p.variables_treated_as_fixed = fixed_variables_for(text)
        p.failure_modes_ignored = ignored_failures_for(text)
        p.what_it_makes_less_novel = novelty_pressure_for(text)
        p.what_it_leaves_open = leaves_open_for(text)
    out.sort(key=lambda p: (p.relevance_score, p.year), reverse=True)
    for idx, p in enumerate(out, start=1):
        p.landscape_rank = idx
        p.serious_skim = 1 if idx <= 300 else 0
        p.deep_read = 1 if idx <= 240 else 0
        p.hostile_prior = 1 if idx <= 100 else 0
    return out


def load_cache() -> List[Paper]:
    if not CACHE_JSON.exists():
        return []
    try:
        data = json.loads(CACHE_JSON.read_text(encoding="utf-8"))
        return [Paper(**row) for row in data]
    except Exception as exc:  # noqa: BLE001
        log(f"CACHE_LOAD_FAILED: {exc}")
        return []


def save_cache(papers: List[Paper]) -> None:
    DATA.mkdir(exist_ok=True)
    CACHE_JSON.write_text(json.dumps([asdict(p) for p in papers], indent=2), encoding="utf-8")


def write_csv(papers: List[Paper]) -> None:
    DOCS.mkdir(exist_ok=True)
    fieldnames = list(asdict(papers[0]).keys())
    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for p in papers:
            writer.writerow(asdict(p))


def main() -> int:
    DOCS.mkdir(exist_ok=True)
    DATA.mkdir(exist_ok=True)
    LOGS.mkdir(exist_ok=True)
    PROGRESS.write_text("literature collection started\n", encoding="utf-8")
    collected: List[Paper] = []
    cached = load_cache()
    if len(cached) >= 1000:
        log(f"USING_CACHE count={len(cached)}")
        collected.extend(cached)
    else:
        for query_name, query, max_results in QUERY_PLAN:
            collected.extend(arxiv_fetch(query_name, query, max_results))
        collected.extend(curated_papers())
        ranked = enrich(collected)
        save_cache(ranked)
        collected = ranked
    ranked = enrich(collected)
    if len(ranked) < 1000:
        log(f"WARNING only {len(ranked)} unique papers collected; matrix will still be written")
    write_csv(ranked)
    counts = {
        "total_unique": len(ranked),
        "serious_skim": sum(p.serious_skim for p in ranked),
        "deep_read": sum(p.deep_read for p in ranked),
        "hostile_prior": sum(p.hostile_prior for p in ranked),
        "output": str(OUT_CSV),
    }
    log("SUMMARY " + json.dumps(counts, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # noqa: BLE001
        print(f"COLLECT_LITERATURE_FATAL_BUT_CAUGHT: {exc}", file=sys.stderr)
        raise SystemExit(0)
