# Literature Map

## Field Box
Robot tool use inside contact-rich manipulation: how an embodied agent represents, plans, and diagnoses physical interactions among hand, tool, target, and environment.

## Sweep Accounting
- Landscape entries in `docs/related_work_matrix.csv`: 1733
- Serious skim proxy: 300 papers
- Deep read proxy: 240 papers
- Hostile prior set: 100 papers

## Source Mix
- arxiv: 1705
- curated: 28

## Dominant Mechanism Families
- Optimization over trajectories, contact modes, or continuous constraints.: 445
- Language-model or vision-language-model decomposition into robot actions.: 345
- Sensing/control loop using tactile, force, or impedance signals.: 303
- Algorithmic robot manipulation model or empirical system.: 303
- Learned policy, dynamics model, representation, or self-supervised predictor.: 239
- Task-and-motion planning with samplers, predicates, and geometric checks.: 59
- Learned or engineered affordance labels, maps, relations, or key regions.: 38
- A symbolic or compositional grammar over actions, contacts, or programs.: 1

## Top Novelty-Pressuring Papers
1. **Learning Granularity-Aware Affordances from Human-Object Interaction for Tool-Based Functional Grasping in Dexterous Robotics** (2024) - static or learned action-region representations; tool-use transfer, task-oriented grasping, and tool design
2. **Robot Tool Use: A Survey** (2023) - tool-use transfer, task-oriented grasping, and tool design
3. **Task-Oriented Grasping with Semantic and Geometric Constraints** (2012) - general robot manipulation representation learning
4. **CALAMARI: Contact-Aware and Language Conditioned Spatial Action Maps for Contact-Rich Manipulation** (2023) - contact-mode planning and contact-rich control; LLM program/planner interfaces for robot manipulation
5. **Towards Tight Convex Relaxations for Contact-Rich Manipulation** (2024) - contact-mode planning and contact-rich control
6. **Learning Task-Oriented Grasping for Tool Manipulation from Simulated Self-Supervision** (2018) - tool-use transfer, task-oriented grasping, and tool design
7. **Learning and Generalization of Behavior-Grounded Tool Affordances** (2007) - static or learned action-region representations; tool-use transfer, task-oriented grasping, and tool design
8. **Planning, Sensing, and Control for Contact-rich Robotic Manipulation** (2023) - contact-mode planning and contact-rich control
9. **A Brief Review of Affordance in Robotic Manipulation Research** (2017) - static or learned action-region representations
10. **Learning to Design and Use Tools for Robotic Manipulation** (2020) - contact-mode planning and contact-rich control; tool-use transfer, task-oriented grasping, and tool design
11. **ContactNets: Learning Discontinuous Contact Dynamics with Smooth, Implicit Representations** (2020) - contact-mode planning and contact-rich control
12. **VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models** (2023) - LLM program/planner interfaces for robot manipulation
13. **Behavior-Grounded Representation of Tool Affordances** (2005) - static or learned action-region representations; tool-use transfer, task-oriented grasping, and tool design
14. **Building Affordance Relations for Robotic Agents: A Review** (2021) - static or learned action-region representations
15. **PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning** (2020) - symbolic precondition/effect planning
16. **Hierarchical Task and Motion Planning in the Now** (2011) - symbolic precondition/effect planning
17. **RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control** (2023) - LLM program/planner interfaces for robot manipulation
18. **Code as Policies: Language Model Programs for Embodied Control** (2023) - LLM program/planner interfaces for robot manipulation
19. **Sequential Composition of Dynamically Dexterous Robot Behaviors** (1999) - general robot manipulation representation learning
20. **Affordances are Versatile Intermediate Representations for Robot Manipulation** (2024) - static or learned action-region representations

## Hidden Assumptions That May Be False
1. Affordance labels can be assigned before the contact sequence is known.
2. A tool's functional part determines use independent of how the robot grips it.
3. Contacts with the same object pair are interchangeable across sides and roles.
4. The environment is a passive obstacle rather than an active mechanical support.
5. Task success can be predicted from object category plus action name.
6. Contact-rich tool use can be handled by searching contact modes after high-level planning.
7. A learned policy will interpolate to unseen compositions of familiar tool parts.
8. Language decompositions preserve force, side, and support preconditions.
9. Task-and-motion predicates expose all mechanically relevant contact roles.
10. Tactile feedback only repairs execution, rather than changing the symbolic plan.
11. Grasp stability and task effectiveness can be optimized independently.
12. One affordance region has one function across target geometries.
13. Tool use is a two-stage pick-then-use process rather than a contact graph over hand, tool, target, and environment.
14. The right abstraction is a state vector or latent embedding, not a typed production rule.
15. Failure is mostly distribution shift, not a falsified physical precondition.
16. Contact order is recoverable from an unordered set of contacts.
17. Compliance can be modeled as noise around rigid contact predictions.
18. Intermediate representations should be descriptive maps rather than generative rules.
19. A planner's no-plan result is less informative than a failed production.
20. Demonstrations teach action chunks, not the hidden contact grammar that makes chunks reusable.
21. Contact grammar is only a notation, not an executable hypothesis class.
22. Novel tools require new data instead of recombining known contact productions.
23. Friction and support assumptions can be left implicit until low-level control.
24. Tool morphology and contact role can be separated cleanly.

## Directions Generated Before Selection
- **Counterfactual affordance maps.** Force an affordance model to predict when the same region becomes invalid under a changed contact order.
- **Contact-role grammar.** Make ordered hand-tool-target-environment contacts the central representation and test each production as a falsifiable rule.
- **Mechanics-first TAMP predicates.** Replace object predicates with mechanically typed supports, pivots, and force-transmission relations.
- **Tool morphology calculus.** Represent tools by reusable mechanical operators rather than category labels or learned embeddings.
- **Failure-language bridge.** Translate contact production failures into language for human repair without using language as the planner.

## Selection
The strongest direction is **contact-role grammar**: represent tool use as typed, ordered productions over contacts, where each production has explicit preconditions and counterfactual failure tests. This changes the central mechanism from static affordance, opaque policy, or mode-search abstraction to a compositional rule system whose rules can be individually falsified.
