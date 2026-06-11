# Hostile Prior Work Set

This is the 100-paper hostile set used to pressure the novelty claim. Each entry records the claimed problem, actual mechanism, hidden assumptions, fixed variables, ignored failures, what becomes less novel, and what remains open.

## 1. Learning Granularity-Aware Affordances from Human-Object Interaction for Tool-Based Functional Grasping in Dexterous Robotics (2024)
- Source: arXiv | https://arxiv.org/abs/2407.00614
- Problem claimed: Enable robots to select, grasp, design, or use tools for physical tasks.
- Actual mechanism introduced: Learned or engineered affordance labels, maps, relations, or key regions.
- Hidden assumptions: affordances can be localized before the full contact sequence is known; tool function is stable across grasp, approach, and target geometry; training distribution covers the relevant contact compositions
- Variables treated as fixed: grasp taxonomy or candidate grasp set
- Failure modes ignored: correct region with wrong contact order; grasp makes the functional end unreachable or reverses the required contact side; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: static or learned action-region representations; tool-use transfer, task-oriented grasping, and tool design
- What it leaves open: a falsifiable account of when the same affordance label fails under a different contact history; generalization from tool parts to ordered tool-target-environment contact productions; distribution-free checks for impossible contact sequences

## 2. Robot Tool Use: A Survey (2023)
- Source: Frontiers in Robotics and AI | https://doi.org/10.3389/frobt.2022.1009488
- Problem claimed: Enable robots to select, grasp, design, or use tools for physical tasks.
- Actual mechanism introduced: Learned policy, dynamics model, representation, or self-supervised predictor.
- Hidden assumptions: tool function is stable across grasp, approach, and target geometry; training distribution covers the relevant contact compositions
- Variables treated as fixed: object geometry, task family, and controller interface
- Failure modes ignored: grasp makes the functional end unreachable or reverses the required contact side; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: tool-use transfer, task-oriented grasping, and tool design
- What it leaves open: generalization from tool parts to ordered tool-target-environment contact productions; distribution-free checks for impossible contact sequences

## 3. Task-Oriented Grasping with Semantic and Geometric Constraints (2012)
- Source: Robotics and Autonomous Systems | https://doi.org/10.1016/j.robot.2012.07.009
- Problem claimed: Improve robot manipulation, planning, or embodied action generalization.
- Actual mechanism introduced: Sensing/control loop using tactile, force, or impedance signals.
- Hidden assumptions: geometry, friction, compliance, and object roles remain within modeled regimes
- Variables treated as fixed: grasp taxonomy or candidate grasp set
- Failure modes ignored: boundary cases where hidden physical preconditions fail
- What it makes less novel: general robot manipulation representation learning
- What it leaves open: explicit contact-role compositionality and falsification tests

## 4. CALAMARI: Contact-Aware and Language Conditioned Spatial Action Maps for Contact-Rich Manipulation (2023)
- Source: CoRL | https://proceedings.mlr.press/v229/wi23a.html
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Language-model or vision-language-model decomposition into robot actions.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; language decompositions preserve physical contact preconditions
- Variables treated as fixed: prompted skill API and object labels
- Failure modes ignored: role-equivalent contacts that induce different mechanics; plausible verbal plan that skips a necessary physical contact
- What it makes less novel: contact-mode planning and contact-rich control; LLM program/planner interfaces for robot manipulation
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools

## 5. Towards Tight Convex Relaxations for Contact-Rich Manipulation (2024)
- Source: RSS | https://roboticsproceedings.org/rss20/p132.html
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Optimization over trajectories, contact modes, or continuous constraints.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift
- Variables treated as fixed: object geometry, task family, and controller interface
- Failure modes ignored: role-equivalent contacts that induce different mechanics
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools

## 6. Learning Task-Oriented Grasping for Tool Manipulation from Simulated Self-Supervision (2018)
- Source: RSS | https://roboticsproceedings.org/rss14/p12.html
- Problem claimed: Enable robots to select, grasp, design, or use tools for physical tasks.
- Actual mechanism introduced: Learned policy, dynamics model, representation, or self-supervised predictor.
- Hidden assumptions: tool function is stable across grasp, approach, and target geometry; training distribution covers the relevant contact compositions
- Variables treated as fixed: grasp taxonomy or candidate grasp set; simulator contact parameters; camera viewpoint and perceptual segmentation quality
- Failure modes ignored: grasp makes the functional end unreachable or reverses the required contact side; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: tool-use transfer, task-oriented grasping, and tool design
- What it leaves open: generalization from tool parts to ordered tool-target-environment contact productions; distribution-free checks for impossible contact sequences

## 7. Learning and Generalization of Behavior-Grounded Tool Affordances (2007)
- Source: IEEE ICDL | https://doi.org/10.1109/DEVLRN.2007.4354064
- Problem claimed: Enable robots to select, grasp, design, or use tools for physical tasks.
- Actual mechanism introduced: Learned or engineered affordance labels, maps, relations, or key regions.
- Hidden assumptions: affordances can be localized before the full contact sequence is known; tool function is stable across grasp, approach, and target geometry; training distribution covers the relevant contact compositions
- Variables treated as fixed: object geometry, task family, and controller interface
- Failure modes ignored: correct region with wrong contact order; grasp makes the functional end unreachable or reverses the required contact side; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: static or learned action-region representations; tool-use transfer, task-oriented grasping, and tool design
- What it leaves open: a falsifiable account of when the same affordance label fails under a different contact history; generalization from tool parts to ordered tool-target-environment contact productions; distribution-free checks for impossible contact sequences

## 8. Planning, Sensing, and Control for Contact-rich Robotic Manipulation (2023)
- Source: PhD Thesis | https://groups.csail.mit.edu/robotics-center/public_papers/Pang23.pdf
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Algorithmic robot manipulation model or empirical system.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift
- Variables treated as fixed: predicate vocabulary and action library
- Failure modes ignored: role-equivalent contacts that induce different mechanics
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; mechanism-level error diagnosis instead of plan/no-plan output

## 9. A Brief Review of Affordance in Robotic Manipulation Research (2017)
- Source: Advanced Robotics | https://doi.org/10.1080/01691864.2017.1394912
- Problem claimed: Represent action possibilities of objects or regions for manipulation.
- Actual mechanism introduced: Learned or engineered affordance labels, maps, relations, or key regions.
- Hidden assumptions: affordances can be localized before the full contact sequence is known
- Variables treated as fixed: grasp taxonomy or candidate grasp set
- Failure modes ignored: correct region with wrong contact order
- What it makes less novel: static or learned action-region representations
- What it leaves open: a falsifiable account of when the same affordance label fails under a different contact history

## 10. Learning to Design and Use Tools for Robotic Manipulation (2020)
- Source: CoRL | https://proceedings.mlr.press/v100/shao20a.html
- Problem claimed: Enable robots to select, grasp, design, or use tools for physical tasks.
- Actual mechanism introduced: Learned policy, dynamics model, representation, or self-supervised predictor.
- Hidden assumptions: tool function is stable across grasp, approach, and target geometry; contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions
- Variables treated as fixed: simulator contact parameters
- Failure modes ignored: role-equivalent contacts that induce different mechanics; grasp makes the functional end unreachable or reverses the required contact side; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: contact-mode planning and contact-rich control; tool-use transfer, task-oriented grasping, and tool design
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; generalization from tool parts to ordered tool-target-environment contact productions; distribution-free checks for impossible contact sequences

## 11. ContactNets: Learning Discontinuous Contact Dynamics with Smooth, Implicit Representations (2020)
- Source: CoRL | https://arxiv.org/abs/2009.11193
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Learned policy, dynamics model, representation, or self-supervised predictor.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions
- Variables treated as fixed: object geometry, task family, and controller interface
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences

## 12. VoxPoser: Composable 3D Value Maps for Robotic Manipulation with Language Models (2023)
- Source: CoRL | https://arxiv.org/abs/2307.05973
- Problem claimed: Ground broad pretrained models in embodied robot actions.
- Actual mechanism introduced: Language-model or vision-language-model decomposition into robot actions.
- Hidden assumptions: language decompositions preserve physical contact preconditions
- Variables treated as fixed: camera viewpoint and perceptual segmentation quality; prompted skill API and object labels
- Failure modes ignored: plausible verbal plan that skips a necessary physical contact
- What it makes less novel: LLM program/planner interfaces for robot manipulation
- What it leaves open: explicit contact-role compositionality and falsification tests

## 13. Behavior-Grounded Representation of Tool Affordances (2005)
- Source: ICRA Workshop | https://home.engineering.iastate.edu/~alexs/papers/ICRA05-WKSP.pdf
- Problem claimed: Enable robots to select, grasp, design, or use tools for physical tasks.
- Actual mechanism introduced: Learned or engineered affordance labels, maps, relations, or key regions.
- Hidden assumptions: affordances can be localized before the full contact sequence is known; tool function is stable across grasp, approach, and target geometry
- Variables treated as fixed: object geometry, task family, and controller interface
- Failure modes ignored: correct region with wrong contact order; grasp makes the functional end unreachable or reverses the required contact side
- What it makes less novel: static or learned action-region representations; tool-use transfer, task-oriented grasping, and tool design
- What it leaves open: a falsifiable account of when the same affordance label fails under a different contact history; generalization from tool parts to ordered tool-target-environment contact productions

## 14. Building Affordance Relations for Robotic Agents: A Review (2021)
- Source: IJCAI | https://doi.org/10.24963/ijcai.2021/590
- Problem claimed: Represent action possibilities of objects or regions for manipulation.
- Actual mechanism introduced: Learned or engineered affordance labels, maps, relations, or key regions.
- Hidden assumptions: affordances can be localized before the full contact sequence is known
- Variables treated as fixed: object geometry, task family, and controller interface
- Failure modes ignored: correct region with wrong contact order
- What it makes less novel: static or learned action-region representations
- What it leaves open: a falsifiable account of when the same affordance label fails under a different contact history

## 15. PDDLStream: Integrating Symbolic Planners and Blackbox Samplers via Optimistic Adaptive Planning (2020)
- Source: ICAPS | https://arxiv.org/abs/1802.08705
- Problem claimed: Bridge symbolic task structure and continuous robot motion feasibility.
- Actual mechanism introduced: Task-and-motion planning with samplers, predicates, and geometric checks.
- Hidden assumptions: predicates expose the contact roles needed by the continuous planner
- Variables treated as fixed: predicate vocabulary and action library
- Failure modes ignored: boundary cases where hidden physical preconditions fail
- What it makes less novel: symbolic precondition/effect planning
- What it leaves open: mechanism-level error diagnosis instead of plan/no-plan output

## 16. Hierarchical Task and Motion Planning in the Now (2011)
- Source: ICRA | https://doi.org/10.1109/ICRA.2011.5980391
- Problem claimed: Bridge symbolic task structure and continuous robot motion feasibility.
- Actual mechanism introduced: Task-and-motion planning with samplers, predicates, and geometric checks.
- Hidden assumptions: predicates expose the contact roles needed by the continuous planner
- Variables treated as fixed: predicate vocabulary and action library
- Failure modes ignored: boundary cases where hidden physical preconditions fail
- What it makes less novel: symbolic precondition/effect planning
- What it leaves open: mechanism-level error diagnosis instead of plan/no-plan output

## 17. RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control (2023)
- Source: arXiv | https://arxiv.org/abs/2307.15818
- Problem claimed: Ground broad pretrained models in embodied robot actions.
- Actual mechanism introduced: Language-model or vision-language-model decomposition into robot actions.
- Hidden assumptions: language decompositions preserve physical contact preconditions
- Variables treated as fixed: camera viewpoint and perceptual segmentation quality; prompted skill API and object labels
- Failure modes ignored: plausible verbal plan that skips a necessary physical contact
- What it makes less novel: LLM program/planner interfaces for robot manipulation
- What it leaves open: explicit contact-role compositionality and falsification tests

## 18. Code as Policies: Language Model Programs for Embodied Control (2023)
- Source: ICRA | https://arxiv.org/abs/2209.07753
- Problem claimed: Ground broad pretrained models in embodied robot actions.
- Actual mechanism introduced: Language-model or vision-language-model decomposition into robot actions.
- Hidden assumptions: training distribution covers the relevant contact compositions; language decompositions preserve physical contact preconditions
- Variables treated as fixed: prompted skill API and object labels
- Failure modes ignored: out-of-distribution tool compositions that require unseen role ordering; plausible verbal plan that skips a necessary physical contact
- What it makes less novel: LLM program/planner interfaces for robot manipulation
- What it leaves open: explicit contact-role compositionality and falsification tests

## 19. Sequential Composition of Dynamically Dexterous Robot Behaviors (1999)
- Source: IJRR | https://doi.org/10.1177/02783649922066385
- Problem claimed: Improve robot manipulation, planning, or embodied action generalization.
- Actual mechanism introduced: Algorithmic robot manipulation model or empirical system.
- Hidden assumptions: geometry, friction, compliance, and object roles remain within modeled regimes
- Variables treated as fixed: object geometry, task family, and controller interface
- Failure modes ignored: boundary cases where hidden physical preconditions fail
- What it makes less novel: general robot manipulation representation learning
- What it leaves open: explicit contact-role compositionality and falsification tests

## 20. Affordances are Versatile Intermediate Representations for Robot Manipulation (2024)
- Source: arXiv | https://arxiv.org/abs/2411.02704
- Problem claimed: Represent action possibilities of objects or regions for manipulation.
- Actual mechanism introduced: Learned or engineered affordance labels, maps, relations, or key regions.
- Hidden assumptions: affordances can be localized before the full contact sequence is known
- Variables treated as fixed: object geometry, task family, and controller interface
- Failure modes ignored: correct region with wrong contact order
- What it makes less novel: static or learned action-region representations
- What it leaves open: a falsifiable account of when the same affordance label fails under a different contact history

## 21. RT-1: Robotics Transformer for Real-World Control at Scale (2022)
- Source: arXiv | https://arxiv.org/abs/2212.06817
- Problem claimed: Ground broad pretrained models in embodied robot actions.
- Actual mechanism introduced: Language-model or vision-language-model decomposition into robot actions.
- Hidden assumptions: training distribution covers the relevant contact compositions; language decompositions preserve physical contact preconditions
- Variables treated as fixed: prompted skill API and object labels
- Failure modes ignored: out-of-distribution tool compositions that require unseen role ordering; plausible verbal plan that skips a necessary physical contact
- What it makes less novel: LLM program/planner interfaces for robot manipulation
- What it leaves open: distribution-free checks for impossible contact sequences

## 22. Do As I Can, Not As I Say: Grounding Language in Robotic Affordances (2022)
- Source: CoRL | https://arxiv.org/abs/2204.01691
- Problem claimed: Represent action possibilities of objects or regions for manipulation.
- Actual mechanism introduced: Learned or engineered affordance labels, maps, relations, or key regions.
- Hidden assumptions: affordances can be localized before the full contact sequence is known; language decompositions preserve physical contact preconditions
- Variables treated as fixed: predicate vocabulary and action library; prompted skill API and object labels
- Failure modes ignored: correct region with wrong contact order; plausible verbal plan that skips a necessary physical contact
- What it makes less novel: static or learned action-region representations; LLM program/planner interfaces for robot manipulation
- What it leaves open: a falsifiable account of when the same affordance label fails under a different contact history; mechanism-level error diagnosis instead of plan/no-plan output

## 23. Affordance Detection for Task-Specific Grasping Using Deep Learning (2017)
- Source: Humanoids | https://doi.org/10.1109/HUMANOIDS.2017.8246892
- Problem claimed: Represent action possibilities of objects or regions for manipulation.
- Actual mechanism introduced: Learned or engineered affordance labels, maps, relations, or key regions.
- Hidden assumptions: affordances can be localized before the full contact sequence is known; training distribution covers the relevant contact compositions
- Variables treated as fixed: grasp taxonomy or candidate grasp set
- Failure modes ignored: correct region with wrong contact order; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: static or learned action-region representations
- What it leaves open: a falsifiable account of when the same affordance label fails under a different contact history; distribution-free checks for impossible contact sequences

## 24. Logic-Geometric Programming: An Optimization-Based Approach to Combined Task and Motion Planning (2015)
- Source: IJCAI | https://www.ijcai.org/Proceedings/15/Papers/154.pdf
- Problem claimed: Bridge symbolic task structure and continuous robot motion feasibility.
- Actual mechanism introduced: Optimization over trajectories, contact modes, or continuous constraints.
- Hidden assumptions: predicates expose the contact roles needed by the continuous planner
- Variables treated as fixed: predicate vocabulary and action library
- Failure modes ignored: boundary cases where hidden physical preconditions fail
- What it makes less novel: symbolic precondition/effect planning
- What it leaves open: mechanism-level error diagnosis instead of plan/no-plan output

## 25. Stable Pushing: Mechanics, Controllability, and Planning (1996)
- Source: IJRR | https://doi.org/10.1177/027836499601500803
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Algorithmic robot manipulation model or empirical system.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift
- Variables treated as fixed: predicate vocabulary and action library
- Failure modes ignored: role-equivalent contacts that induce different mechanics
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; mechanism-level error diagnosis instead of plan/no-plan output

## 26. An Exploration of Sensorless Manipulation (1988)
- Source: IEEE Journal on Robotics and Automation | https://doi.org/10.1109/56.805
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Algorithmic robot manipulation model or empirical system.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift
- Variables treated as fixed: object geometry, task family, and controller interface
- Failure modes ignored: role-equivalent contacts that induce different mechanics
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools

## 27. Mechanics and Planning of Manipulator Pushing Operations (1986)
- Source: IJRR | https://doi.org/10.1177/027836498600500303
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Algorithmic robot manipulation model or empirical system.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift
- Variables treated as fixed: predicate vocabulary and action library
- Failure modes ignored: role-equivalent contacts that induce different mechanics
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; mechanism-level error diagnosis instead of plan/no-plan output

## 28. The Ecological Approach to Visual Perception (1979)
- Source: Book | https://www.routledge.com/The-Ecological-Approach-to-Visual-Perception/Gibson/p/book/9781848725782
- Problem claimed: Represent action possibilities of objects or regions for manipulation.
- Actual mechanism introduced: Learned or engineered affordance labels, maps, relations, or key regions.
- Hidden assumptions: affordances can be localized before the full contact sequence is known
- Variables treated as fixed: object geometry, task family, and controller interface
- Failure modes ignored: correct region with wrong contact order
- What it makes less novel: static or learned action-region representations
- What it leaves open: a falsifiable account of when the same affordance label fails under a different contact history

## 29. Physics-Conditioned Grasping for Stable Tool Use (2025)
- Source: arXiv | http://arxiv.org/abs/2505.01399v3
- Problem claimed: Enable robots to select, grasp, design, or use tools for physical tasks.
- Actual mechanism introduced: Optimization over trajectories, contact modes, or continuous constraints.
- Hidden assumptions: tool function is stable across grasp, approach, and target geometry; contact mode abstractions are available or can be searched without semantic role drift; language decompositions preserve physical contact preconditions
- Variables treated as fixed: grasp taxonomy or candidate grasp set; simulator contact parameters; camera viewpoint and perceptual segmentation quality; predicate vocabulary and action library; prompted skill API and object labels
- Failure modes ignored: role-equivalent contacts that induce different mechanics; grasp makes the functional end unreachable or reverses the required contact side; plausible verbal plan that skips a necessary physical contact
- What it makes less novel: contact-mode planning and contact-rich control; tool-use transfer, task-oriented grasping, and tool design; LLM program/planner interfaces for robot manipulation
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; generalization from tool parts to ordered tool-target-environment contact productions; mechanism-level error diagnosis instead of plan/no-plan output

## 30. MagicGripper: A Multimodal Sensor-Integrated Gripper for Contact-Rich Robotic Manipulation (2025)
- Source: arXiv | http://arxiv.org/abs/2505.24382v1
- Problem claimed: Enable robots to select, grasp, design, or use tools for physical tasks.
- Actual mechanism introduced: Sensing/control loop using tactile, force, or impedance signals.
- Hidden assumptions: tool function is stable across grasp, approach, and target geometry; contact mode abstractions are available or can be searched without semantic role drift
- Variables treated as fixed: grasp taxonomy or candidate grasp set; camera viewpoint and perceptual segmentation quality
- Failure modes ignored: role-equivalent contacts that induce different mechanics; grasp makes the functional end unreachable or reverses the required contact side
- What it makes less novel: contact-mode planning and contact-rich control; tool-use transfer, task-oriented grasping, and tool design
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; generalization from tool parts to ordered tool-target-environment contact productions

## 31. UNIC: Learning Unified Multimodal Extrinsic Contact Estimation (2026)
- Source: arXiv | http://arxiv.org/abs/2601.04356v2
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Learned or engineered affordance labels, maps, relations, or key regions.
- Hidden assumptions: affordances can be localized before the full contact sequence is known; contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions
- Variables treated as fixed: grasp taxonomy or candidate grasp set; predicate vocabulary and action library
- Failure modes ignored: correct region with wrong contact order; role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: static or learned action-region representations; contact-mode planning and contact-rich control
- What it leaves open: a falsifiable account of when the same affordance label fails under a different contact history; a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences; mechanism-level error diagnosis instead of plan/no-plan output

## 32. IMPACT: Learning Internal-Model Predictive Control for Forceful Robotic Manipulation (2026)
- Source: arXiv | http://arxiv.org/abs/2606.10818v1
- Problem claimed: Enable robots to select, grasp, design, or use tools for physical tasks.
- Actual mechanism introduced: Sensing/control loop using tactile, force, or impedance signals.
- Hidden assumptions: tool function is stable across grasp, approach, and target geometry; contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions
- Variables treated as fixed: simulator contact parameters; predicate vocabulary and action library
- Failure modes ignored: role-equivalent contacts that induce different mechanics; grasp makes the functional end unreachable or reverses the required contact side; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: contact-mode planning and contact-rich control; tool-use transfer, task-oriented grasping, and tool design
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; generalization from tool parts to ordered tool-target-environment contact productions; distribution-free checks for impossible contact sequences; mechanism-level error diagnosis instead of plan/no-plan output

## 33. BridgeACT: Bridging Human Demonstrations to Robot Actions via Unified Tool-Target Affordances (2026)
- Source: arXiv | http://arxiv.org/abs/2604.23249v2
- Problem claimed: Enable robots to select, grasp, design, or use tools for physical tasks.
- Actual mechanism introduced: Learned or engineered affordance labels, maps, relations, or key regions.
- Hidden assumptions: affordances can be localized before the full contact sequence is known; tool function is stable across grasp, approach, and target geometry; training distribution covers the relevant contact compositions
- Variables treated as fixed: grasp taxonomy or candidate grasp set
- Failure modes ignored: correct region with wrong contact order; grasp makes the functional end unreachable or reverses the required contact side; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: static or learned action-region representations; tool-use transfer, task-oriented grasping, and tool design
- What it leaves open: a falsifiable account of when the same affordance label fails under a different contact history; generalization from tool parts to ordered tool-target-environment contact productions; distribution-free checks for impossible contact sequences

## 34. Master Micro Residual Correction with Adaptive Tactile Fusion and Force-Mixed Control for Contact-Rich Manipulation (2026)
- Source: arXiv | http://arxiv.org/abs/2603.15152v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Sensing/control loop using tactile, force, or impedance signals.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions
- Variables treated as fixed: grasp taxonomy or candidate grasp set; simulator contact parameters; camera viewpoint and perceptual segmentation quality; predicate vocabulary and action library
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences; mechanism-level error diagnosis instead of plan/no-plan output

## 35. Safe Learning for Contact-Rich Robot Tasks: A Survey from Classical Learning-Based Methods to Safe Foundation Models (2025)
- Source: arXiv | http://arxiv.org/abs/2512.11908v2
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Optimization over trajectories, contact modes, or continuous constraints.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions; language decompositions preserve physical contact preconditions
- Variables treated as fixed: camera viewpoint and perceptual segmentation quality; prompted skill API and object labels
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering; plausible verbal plan that skips a necessary physical contact
- What it makes less novel: contact-mode planning and contact-rich control; LLM program/planner interfaces for robot manipulation
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences

## 36. Touch begins where vision ends: Generalizable policies for contact-rich manipulation (2025)
- Source: arXiv | http://arxiv.org/abs/2506.13762v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Language-model or vision-language-model decomposition into robot actions.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions; language decompositions preserve physical contact preconditions
- Variables treated as fixed: camera viewpoint and perceptual segmentation quality; prompted skill API and object labels
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering; plausible verbal plan that skips a necessary physical contact
- What it makes less novel: contact-mode planning and contact-rich control; LLM program/planner interfaces for robot manipulation
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences

## 37. LEMMo-Plan: LLM-Enhanced Learning from Multi-Modal Demonstration for Planning Sequential Contact-Rich Manipulation Tasks (2024)
- Source: arXiv | http://arxiv.org/abs/2409.11863v2
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Language-model or vision-language-model decomposition into robot actions.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions; language decompositions preserve physical contact preconditions
- Variables treated as fixed: predicate vocabulary and action library; prompted skill API and object labels
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering; plausible verbal plan that skips a necessary physical contact
- What it makes less novel: contact-mode planning and contact-rich control; LLM program/planner interfaces for robot manipulation
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences; mechanism-level error diagnosis instead of plan/no-plan output

## 38. Probabilistic Framework for Constrained Manipulations and Task and Motion Planning under Uncertainty (2020)
- Source: arXiv | http://arxiv.org/abs/2003.04259v1
- Problem claimed: Enable robots to select, grasp, design, or use tools for physical tasks.
- Actual mechanism introduced: Optimization over trajectories, contact modes, or continuous constraints.
- Hidden assumptions: tool function is stable across grasp, approach, and target geometry; contact mode abstractions are available or can be searched without semantic role drift; predicates expose the contact roles needed by the continuous planner
- Variables treated as fixed: grasp taxonomy or candidate grasp set; predicate vocabulary and action library
- Failure modes ignored: role-equivalent contacts that induce different mechanics; grasp makes the functional end unreachable or reverses the required contact side
- What it makes less novel: contact-mode planning and contact-rich control; tool-use transfer, task-oriented grasping, and tool design; symbolic precondition/effect planning
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; generalization from tool parts to ordered tool-target-environment contact productions; mechanism-level error diagnosis instead of plan/no-plan output

## 39. HapticVLA: Contact-Rich Manipulation via Vision-Language-Action Model without Inference-Time Tactile Sensing (2026)
- Source: arXiv | http://arxiv.org/abs/2603.15257v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Language-model or vision-language-model decomposition into robot actions.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; language decompositions preserve physical contact preconditions
- Variables treated as fixed: grasp taxonomy or candidate grasp set; camera viewpoint and perceptual segmentation quality; prompted skill API and object labels
- Failure modes ignored: role-equivalent contacts that induce different mechanics; plausible verbal plan that skips a necessary physical contact
- What it makes less novel: contact-mode planning and contact-rich control; LLM program/planner interfaces for robot manipulation
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools

## 40. A Realistic Surgical Simulator for Non-Rigid and Contact-Rich Manipulation in Surgeries with the da Vinci Research Kit (2024)
- Source: arXiv | http://arxiv.org/abs/2404.05888v2
- Problem claimed: Enable robots to select, grasp, design, or use tools for physical tasks.
- Actual mechanism introduced: Learned policy, dynamics model, representation, or self-supervised predictor.
- Hidden assumptions: tool function is stable across grasp, approach, and target geometry; contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions
- Variables treated as fixed: grasp taxonomy or candidate grasp set; simulator contact parameters
- Failure modes ignored: role-equivalent contacts that induce different mechanics; grasp makes the functional end unreachable or reverses the required contact side; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: contact-mode planning and contact-rich control; tool-use transfer, task-oriented grasping, and tool design
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; generalization from tool parts to ordered tool-target-environment contact productions; distribution-free checks for impossible contact sequences

## 41. Just Add Force for Contact-Rich Robot Policies (2024)
- Source: arXiv | http://arxiv.org/abs/2410.13124v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Language-model or vision-language-model decomposition into robot actions.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions; language decompositions preserve physical contact preconditions
- Variables treated as fixed: grasp taxonomy or candidate grasp set; camera viewpoint and perceptual segmentation quality; prompted skill API and object labels
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering; plausible verbal plan that skips a necessary physical contact
- What it makes less novel: contact-mode planning and contact-rich control; LLM program/planner interfaces for robot manipulation
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences

## 42. Learning to Feel the Future: DreamTacVLA for Contact-Rich Manipulation (2025)
- Source: arXiv | http://arxiv.org/abs/2512.23864v3
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Language-model or vision-language-model decomposition into robot actions.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions; language decompositions preserve physical contact preconditions
- Variables treated as fixed: camera viewpoint and perceptual segmentation quality; prompted skill API and object labels
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering; plausible verbal plan that skips a necessary physical contact
- What it makes less novel: contact-mode planning and contact-rich control; LLM program/planner interfaces for robot manipulation
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences

## 43. CLTP: Contrastive Language-Tactile Pre-training for 3D Contact Geometry Understanding (2025)
- Source: arXiv | http://arxiv.org/abs/2505.08194v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Language-model or vision-language-model decomposition into robot actions.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions; language decompositions preserve physical contact preconditions
- Variables treated as fixed: camera viewpoint and perceptual segmentation quality; prompted skill API and object labels
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering; plausible verbal plan that skips a necessary physical contact
- What it makes less novel: contact-mode planning and contact-rich control; LLM program/planner interfaces for robot manipulation
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences

## 44. AffordSim: A Scalable Data Generator and Benchmark for Affordance-Aware Robotic Manipulation (2026)
- Source: arXiv | http://arxiv.org/abs/2604.11674v2
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Optimization over trajectories, contact modes, or continuous constraints.
- Hidden assumptions: affordances can be localized before the full contact sequence is known; contact mode abstractions are available or can be searched without semantic role drift; language decompositions preserve physical contact preconditions
- Variables treated as fixed: grasp taxonomy or candidate grasp set; simulator contact parameters; camera viewpoint and perceptual segmentation quality; predicate vocabulary and action library; prompted skill API and object labels
- Failure modes ignored: correct region with wrong contact order; role-equivalent contacts that induce different mechanics; plausible verbal plan that skips a necessary physical contact
- What it makes less novel: static or learned action-region representations; contact-mode planning and contact-rich control; LLM program/planner interfaces for robot manipulation
- What it leaves open: a falsifiable account of when the same affordance label fails under a different contact history; a compact symbolic language for role-typed contact transitions across tools; mechanism-level error diagnosis instead of plan/no-plan output

## 45. KinDER: A Physical Reasoning Benchmark for Robot Learning and Planning (2026)
- Source: arXiv | http://arxiv.org/abs/2604.25788v2
- Problem claimed: Enable robots to select, grasp, design, or use tools for physical tasks.
- Actual mechanism introduced: Language-model or vision-language-model decomposition into robot actions.
- Hidden assumptions: tool function is stable across grasp, approach, and target geometry; training distribution covers the relevant contact compositions; language decompositions preserve physical contact preconditions; predicates expose the contact roles needed by the continuous planner
- Variables treated as fixed: simulator contact parameters; predicate vocabulary and action library; prompted skill API and object labels
- Failure modes ignored: grasp makes the functional end unreachable or reverses the required contact side; out-of-distribution tool compositions that require unseen role ordering; plausible verbal plan that skips a necessary physical contact
- What it makes less novel: tool-use transfer, task-oriented grasping, and tool design; symbolic precondition/effect planning; LLM program/planner interfaces for robot manipulation
- What it leaves open: generalization from tool parts to ordered tool-target-environment contact productions; distribution-free checks for impossible contact sequences; mechanism-level error diagnosis instead of plan/no-plan output

## 46. TacForeSight: Force-Guided Tactile World Model for Contact-Rich Manipulation (2026)
- Source: arXiv | http://arxiv.org/abs/2606.11184v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Sensing/control loop using tactile, force, or impedance signals.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions
- Variables treated as fixed: object geometry, task family, and controller interface
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences

## 47. OmniVTA: Visuo-Tactile World Modeling for Contact-Rich Robotic Manipulation (2026)
- Source: arXiv | http://arxiv.org/abs/2603.19201v2
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Sensing/control loop using tactile, force, or impedance signals.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions
- Variables treated as fixed: camera viewpoint and perceptual segmentation quality
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools

## 48. Contact-aware Shaping and Maintenance of Deformable Linear Objects With Fixtures (2023)
- Source: arXiv | http://arxiv.org/abs/2307.10153v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Sensing/control loop using tactile, force, or impedance signals.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; predicates expose the contact roles needed by the continuous planner
- Variables treated as fixed: predicate vocabulary and action library
- Failure modes ignored: role-equivalent contacts that induce different mechanics
- What it makes less novel: contact-mode planning and contact-rich control; symbolic precondition/effect planning
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; mechanism-level error diagnosis instead of plan/no-plan output

## 49. DIFFTACTILE: A Physics-based Differentiable Tactile Simulator for Contact-rich Robotic Manipulation (2024)
- Source: arXiv | http://arxiv.org/abs/2403.08716v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Optimization over trajectories, contact modes, or continuous constraints.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions
- Variables treated as fixed: grasp taxonomy or candidate grasp set; simulator contact parameters
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences

## 50. Robustness-Aware Tool Selection and Manipulation Planning with Learned Energy-Informed Guidance (2025)
- Source: arXiv | http://arxiv.org/abs/2506.03362v2
- Problem claimed: Enable robots to select, grasp, design, or use tools for physical tasks.
- Actual mechanism introduced: Optimization over trajectories, contact modes, or continuous constraints.
- Hidden assumptions: tool function is stable across grasp, approach, and target geometry; contact mode abstractions are available or can be searched without semantic role drift
- Variables treated as fixed: simulator contact parameters; predicate vocabulary and action library
- Failure modes ignored: role-equivalent contacts that induce different mechanics; grasp makes the functional end unreachable or reverses the required contact side
- What it makes less novel: contact-mode planning and contact-rich control; tool-use transfer, task-oriented grasping, and tool design
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; generalization from tool parts to ordered tool-target-environment contact productions; mechanism-level error diagnosis instead of plan/no-plan output

## 51. A Low-Cost Vision-Based Tactile Gripper with Pretraining Learning for Contact-Rich Manipulation (2026)
- Source: arXiv | http://arxiv.org/abs/2602.00514v2
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Sensing/control loop using tactile, force, or impedance signals.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions
- Variables treated as fixed: grasp taxonomy or candidate grasp set; camera viewpoint and perceptual segmentation quality
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences

## 52. SynManDex: Synthesizing Human-like Dexterous Grasps from Synthetic Human Pre-Grasps (2026)
- Source: arXiv | http://arxiv.org/abs/2606.09798v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Optimization over trajectories, contact modes, or continuous constraints.
- Hidden assumptions: affordances can be localized before the full contact sequence is known; contact mode abstractions are available or can be searched without semantic role drift
- Variables treated as fixed: grasp taxonomy or candidate grasp set; simulator contact parameters
- Failure modes ignored: correct region with wrong contact order; role-equivalent contacts that induce different mechanics
- What it makes less novel: static or learned action-region representations; contact-mode planning and contact-rich control
- What it leaves open: a falsifiable account of when the same affordance label fails under a different contact history; a compact symbolic language for role-typed contact transitions across tools

## 53. HapTile: A Haptic-Informed Vision-Tactile-Language-Action Dataset for Contact-Rich Imitation Learning (2026)
- Source: arXiv | http://arxiv.org/abs/2606.04825v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Optimization over trajectories, contact modes, or continuous constraints.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions; language decompositions preserve physical contact preconditions
- Variables treated as fixed: camera viewpoint and perceptual segmentation quality; prompted skill API and object labels
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering; plausible verbal plan that skips a necessary physical contact
- What it makes less novel: contact-mode planning and contact-rich control; LLM program/planner interfaces for robot manipulation
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences

## 54. ETac: A Lightweight and Efficient Tactile Simulation Framework for Learning Dexterous Manipulation (2026)
- Source: arXiv | http://arxiv.org/abs/2604.20295v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Sensing/control loop using tactile, force, or impedance signals.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions
- Variables treated as fixed: grasp taxonomy or candidate grasp set; simulator contact parameters
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences

## 55. DexTac: Learning Contact-aware Visuotactile Policies via Hand-by-hand Teaching (2026)
- Source: arXiv | http://arxiv.org/abs/2601.21474v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Sensing/control loop using tactile, force, or impedance signals.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions
- Variables treated as fixed: object geometry, task family, and controller interface
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences

## 56. TacSL: A Library for Visuotactile Sensor Simulation and Learning (2024)
- Source: arXiv | http://arxiv.org/abs/2408.06506v2
- Problem claimed: Enable robots to select, grasp, design, or use tools for physical tasks.
- Actual mechanism introduced: Sensing/control loop using tactile, force, or impedance signals.
- Hidden assumptions: tool function is stable across grasp, approach, and target geometry; contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions
- Variables treated as fixed: simulator contact parameters; camera viewpoint and perceptual segmentation quality
- Failure modes ignored: role-equivalent contacts that induce different mechanics; grasp makes the functional end unreachable or reverses the required contact side; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: contact-mode planning and contact-rich control; tool-use transfer, task-oriented grasping, and tool design
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; generalization from tool parts to ordered tool-target-environment contact productions; distribution-free checks for impossible contact sequences

## 57. A Digital Twin Framework for Virtual Visuo-Haptic Teleoperation of Complex-Shaped Optical Microrobots (2026)
- Source: arXiv | http://arxiv.org/abs/2605.28448v1
- Problem claimed: Enable robots to select, grasp, design, or use tools for physical tasks.
- Actual mechanism introduced: Sensing/control loop using tactile, force, or impedance signals.
- Hidden assumptions: tool function is stable across grasp, approach, and target geometry; contact mode abstractions are available or can be searched without semantic role drift
- Variables treated as fixed: simulator contact parameters; camera viewpoint and perceptual segmentation quality
- Failure modes ignored: role-equivalent contacts that induce different mechanics; grasp makes the functional end unreachable or reverses the required contact side
- What it makes less novel: contact-mode planning and contact-rich control; tool-use transfer, task-oriented grasping, and tool design
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; generalization from tool parts to ordered tool-target-environment contact productions

## 58. CoRAL: Contact-Rich Adaptive LLM-based Control for Robotic Manipulation (2026)
- Source: arXiv | http://arxiv.org/abs/2605.02600v2
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Language-model or vision-language-model decomposition into robot actions.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; language decompositions preserve physical contact preconditions; predicates expose the contact roles needed by the continuous planner
- Variables treated as fixed: simulator contact parameters; camera viewpoint and perceptual segmentation quality; predicate vocabulary and action library; prompted skill API and object labels
- Failure modes ignored: role-equivalent contacts that induce different mechanics; plausible verbal plan that skips a necessary physical contact
- What it makes less novel: contact-mode planning and contact-rich control; symbolic precondition/effect planning; LLM program/planner interfaces for robot manipulation
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; mechanism-level error diagnosis instead of plan/no-plan output

## 59. Lang2Manip: A Tool for LLM-Based Symbolic-to-Geometric Planning for Manipulation (2025)
- Source: arXiv | http://arxiv.org/abs/2512.17062v1
- Problem claimed: Enable robots to select, grasp, design, or use tools for physical tasks.
- Actual mechanism introduced: Language-model or vision-language-model decomposition into robot actions.
- Hidden assumptions: tool function is stable across grasp, approach, and target geometry; language decompositions preserve physical contact preconditions; predicates expose the contact roles needed by the continuous planner
- Variables treated as fixed: simulator contact parameters; predicate vocabulary and action library; prompted skill API and object labels
- Failure modes ignored: grasp makes the functional end unreachable or reverses the required contact side; plausible verbal plan that skips a necessary physical contact
- What it makes less novel: tool-use transfer, task-oriented grasping, and tool design; symbolic precondition/effect planning; LLM program/planner interfaces for robot manipulation
- What it leaves open: generalization from tool parts to ordered tool-target-environment contact productions; mechanism-level error diagnosis instead of plan/no-plan output

## 60. GenCHiP: Generating Robot Policy Code for High-Precision and Contact-Rich Manipulation Tasks (2024)
- Source: arXiv | http://arxiv.org/abs/2404.06645v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Language-model or vision-language-model decomposition into robot actions.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions; language decompositions preserve physical contact preconditions
- Variables treated as fixed: grasp taxonomy or candidate grasp set; prompted skill API and object labels
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering; plausible verbal plan that skips a necessary physical contact
- What it makes less novel: contact-mode planning and contact-rich control; LLM program/planner interfaces for robot manipulation
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools

## 61. TORL-VLA: Tactile Guided Online Reinforcement Learning for Contact-Rich Manipulation (2026)
- Source: arXiv | http://arxiv.org/abs/2606.09337v2
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Language-model or vision-language-model decomposition into robot actions.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions; language decompositions preserve physical contact preconditions
- Variables treated as fixed: camera viewpoint and perceptual segmentation quality; prompted skill API and object labels
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering; plausible verbal plan that skips a necessary physical contact
- What it makes less novel: contact-mode planning and contact-rich control; LLM program/planner interfaces for robot manipulation
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences

## 62. Learning Tool Morphology for Contact-Rich Manipulation Tasks with Differentiable Simulation (2022)
- Source: arXiv | http://arxiv.org/abs/2211.02201v2
- Problem claimed: Enable robots to select, grasp, design, or use tools for physical tasks.
- Actual mechanism introduced: Optimization over trajectories, contact modes, or continuous constraints.
- Hidden assumptions: tool function is stable across grasp, approach, and target geometry; contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions
- Variables treated as fixed: grasp taxonomy or candidate grasp set; simulator contact parameters
- Failure modes ignored: role-equivalent contacts that induce different mechanics; grasp makes the functional end unreachable or reverses the required contact side; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: contact-mode planning and contact-rich control; tool-use transfer, task-oriented grasping, and tool design
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; generalization from tool parts to ordered tool-target-environment contact productions; distribution-free checks for impossible contact sequences

## 63. Reactive Diffusion Policy: Slow-Fast Visual-Tactile Policy Learning for Contact-Rich Manipulation (2025)
- Source: arXiv | http://arxiv.org/abs/2503.02881v3
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Optimization over trajectories, contact modes, or continuous constraints.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions
- Variables treated as fixed: camera viewpoint and perceptual segmentation quality
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences

## 64. OmniUMI: Towards Physically Grounded Robot Learning via Human-Aligned Multimodal Interaction (2026)
- Source: arXiv | http://arxiv.org/abs/2604.10647v3
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Optimization over trajectories, contact modes, or continuous constraints.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions
- Variables treated as fixed: grasp taxonomy or candidate grasp set; camera viewpoint and perceptual segmentation quality
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences

## 65. PhaForce: Phase-Scheduled Visual-Force Policy Learning with Slow Planning and Fast Correction for Contact-Rich Manipulation (2026)
- Source: arXiv | http://arxiv.org/abs/2603.08342v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Sensing/control loop using tactile, force, or impedance signals.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions
- Variables treated as fixed: camera viewpoint and perceptual segmentation quality; predicate vocabulary and action library
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences; mechanism-level error diagnosis instead of plan/no-plan output

## 66. Gentle Manipulation Policy Learning via Demonstrations from VLM Planned Atomic Skills (2025)
- Source: arXiv | http://arxiv.org/abs/2511.05855v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Language-model or vision-language-model decomposition into robot actions.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions; language decompositions preserve physical contact preconditions
- Variables treated as fixed: simulator contact parameters; predicate vocabulary and action library; prompted skill API and object labels
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering; plausible verbal plan that skips a necessary physical contact
- What it makes less novel: contact-mode planning and contact-rich control; LLM program/planner interfaces for robot manipulation
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences; mechanism-level error diagnosis instead of plan/no-plan output

## 67. ForceFlow: Learning to Feel and Act via Contact-Driven Flow Matching (2026)
- Source: arXiv | http://arxiv.org/abs/2605.11048v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Sensing/control loop using tactile, force, or impedance signals.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions
- Variables treated as fixed: simulator contact parameters; camera viewpoint and perceptual segmentation quality
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences

## 68. CompliantVLA-adaptor: VLM-Guided Variable Impedance Action for Safe Contact-Rich Manipulation (2026)
- Source: arXiv | http://arxiv.org/abs/2601.15541v2
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Language-model or vision-language-model decomposition into robot actions.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; language decompositions preserve physical contact preconditions
- Variables treated as fixed: simulator contact parameters; camera viewpoint and perceptual segmentation quality; prompted skill API and object labels
- Failure modes ignored: role-equivalent contacts that induce different mechanics; plausible verbal plan that skips a necessary physical contact
- What it makes less novel: contact-mode planning and contact-rich control; LLM program/planner interfaces for robot manipulation
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools

## 69. RH20T: A Comprehensive Robotic Dataset for Learning Diverse Skills in One-Shot (2023)
- Source: arXiv | http://arxiv.org/abs/2307.00595v2
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Language-model or vision-language-model decomposition into robot actions.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions; language decompositions preserve physical contact preconditions; predicates expose the contact roles needed by the continuous planner
- Variables treated as fixed: simulator contact parameters; predicate vocabulary and action library; prompted skill API and object labels
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering; plausible verbal plan that skips a necessary physical contact
- What it makes less novel: contact-mode planning and contact-rich control; symbolic precondition/effect planning; LLM program/planner interfaces for robot manipulation
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences; mechanism-level error diagnosis instead of plan/no-plan output

## 70. Admittance Visuomotor Policy Learning for General-Purpose Contact-Rich Manipulations (2024)
- Source: arXiv | http://arxiv.org/abs/2409.14440v2
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Sensing/control loop using tactile, force, or impedance signals.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions
- Variables treated as fixed: grasp taxonomy or candidate grasp set; camera viewpoint and perceptual segmentation quality
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences

## 71. ARISTO Hand: Sensing-Driven Distal Hyperextension for Fine-Grained Manipulation (2026)
- Source: arXiv | http://arxiv.org/abs/2605.30508v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Sensing/control loop using tactile, force, or impedance signals.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift
- Variables treated as fixed: grasp taxonomy or candidate grasp set
- Failure modes ignored: role-equivalent contacts that induce different mechanics
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools

## 72. Versatile Multi-Contact Planning and Control for Legged Loco-Manipulation (2023)
- Source: arXiv | http://arxiv.org/abs/2308.09179v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Optimization over trajectories, contact modes, or continuous constraints.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; predicates expose the contact roles needed by the continuous planner
- Variables treated as fixed: predicate vocabulary and action library
- Failure modes ignored: role-equivalent contacts that induce different mechanics
- What it makes less novel: contact-mode planning and contact-rich control; symbolic precondition/effect planning
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; mechanism-level error diagnosis instead of plan/no-plan output

## 73. ForceVLA2: Unleashing Hybrid Force-Position Control with Force Awareness for Contact-Rich Manipulation (2026)
- Source: arXiv | http://arxiv.org/abs/2603.15169v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Language-model or vision-language-model decomposition into robot actions.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions; language decompositions preserve physical contact preconditions
- Variables treated as fixed: camera viewpoint and perceptual segmentation quality; prompted skill API and object labels
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering; plausible verbal plan that skips a necessary physical contact
- What it makes less novel: contact-mode planning and contact-rich control; LLM program/planner interfaces for robot manipulation
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences

## 74. A Survey on Imitation Learning for Contact-Rich Tasks in Robotics (2025)
- Source: arXiv | http://arxiv.org/abs/2506.13498v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Learned policy, dynamics model, representation, or self-supervised predictor.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions
- Variables treated as fixed: object geometry, task family, and controller interface
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences

## 75. GraspFoM: Towards Reconstruction-Driven Robotic Grasping with 3D Foundation Priors (2026)
- Source: arXiv | http://arxiv.org/abs/2606.08440v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Learned or engineered affordance labels, maps, relations, or key regions.
- Hidden assumptions: affordances can be localized before the full contact sequence is known; contact mode abstractions are available or can be searched without semantic role drift
- Variables treated as fixed: grasp taxonomy or candidate grasp set; camera viewpoint and perceptual segmentation quality
- Failure modes ignored: correct region with wrong contact order; role-equivalent contacts that induce different mechanics
- What it makes less novel: static or learned action-region representations; contact-mode planning and contact-rich control
- What it leaves open: a falsifiable account of when the same affordance label fails under a different contact history; a compact symbolic language for role-typed contact transitions across tools

## 76. Is Linear Feedback on Smoothed Dynamics Sufficient for Stabilizing Contact-Rich Plans? (2024)
- Source: arXiv | http://arxiv.org/abs/2411.06542v4
- Problem claimed: Enable robots to select, grasp, design, or use tools for physical tasks.
- Actual mechanism introduced: Algorithmic robot manipulation model or empirical system.
- Hidden assumptions: tool function is stable across grasp, approach, and target geometry; contact mode abstractions are available or can be searched without semantic role drift
- Variables treated as fixed: simulator contact parameters
- Failure modes ignored: role-equivalent contacts that induce different mechanics; grasp makes the functional end unreachable or reverses the required contact side
- What it makes less novel: contact-mode planning and contact-rich control; tool-use transfer, task-oriented grasping, and tool design
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; generalization from tool parts to ordered tool-target-environment contact productions

## 77. Use the Force, Bot! -- Force-Aware ProDMP with Event-Based Replanning (2024)
- Source: arXiv | http://arxiv.org/abs/2409.11144v1
- Problem claimed: Enable robots to select, grasp, design, or use tools for physical tasks.
- Actual mechanism introduced: Optimization over trajectories, contact modes, or continuous constraints.
- Hidden assumptions: tool function is stable across grasp, approach, and target geometry; contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions
- Variables treated as fixed: predicate vocabulary and action library
- Failure modes ignored: role-equivalent contacts that induce different mechanics; grasp makes the functional end unreachable or reverses the required contact side; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: contact-mode planning and contact-rich control; tool-use transfer, task-oriented grasping, and tool design
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; generalization from tool parts to ordered tool-target-environment contact productions; distribution-free checks for impossible contact sequences; mechanism-level error diagnosis instead of plan/no-plan output

## 78. Dream-Tac: A Unified Tactile World Action Model for Contact-Rich Robot Manipulation (2026)
- Source: arXiv | http://arxiv.org/abs/2606.08737v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Sensing/control loop using tactile, force, or impedance signals.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift
- Variables treated as fixed: camera viewpoint and perceptual segmentation quality
- Failure modes ignored: role-equivalent contacts that induce different mechanics
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools

## 79. Static and Dynamic Representations for Tactile Contact-Angle Estimation with Event-Based Sensors (2026)
- Source: arXiv | http://arxiv.org/abs/2606.03545v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Sensing/control loop using tactile, force, or impedance signals.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift
- Variables treated as fixed: object geometry, task family, and controller interface
- Failure modes ignored: role-equivalent contacts that induce different mechanics
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools

## 80. FlowTouch: View-Invariant Visuo-Tactile Prediction (2026)
- Source: arXiv | http://arxiv.org/abs/2603.08255v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Sensing/control loop using tactile, force, or impedance signals.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift
- Variables treated as fixed: grasp taxonomy or candidate grasp set; simulator contact parameters; camera viewpoint and perceptual segmentation quality; predicate vocabulary and action library
- Failure modes ignored: role-equivalent contacts that induce different mechanics
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; mechanism-level error diagnosis instead of plan/no-plan output

## 81. Glovity: Learning Dexterous Contact-Rich Manipulation via Spatial Wrench Feedback Teleoperation System (2025)
- Source: arXiv | http://arxiv.org/abs/2510.09229v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Sensing/control loop using tactile, force, or impedance signals.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions
- Variables treated as fixed: grasp taxonomy or candidate grasp set
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences

## 82. DexSkin: High-Coverage Conformable Robotic Skin for Learning Contact-Rich Manipulation (2025)
- Source: arXiv | http://arxiv.org/abs/2509.18830v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Sensing/control loop using tactile, force, or impedance signals.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions
- Variables treated as fixed: object geometry, task family, and controller interface
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences

## 83. FreeTacMan: Robot-free Visuo-Tactile Data Collection System for Contact-rich Manipulation (2025)
- Source: arXiv | http://arxiv.org/abs/2506.01941v4
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Sensing/control loop using tactile, force, or impedance signals.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions
- Variables treated as fixed: simulator contact parameters; camera viewpoint and perceptual segmentation quality
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences

## 84. ViTaMIn: Learning Contact-Rich Tasks Through Robot-Free Visuo-Tactile Manipulation Interface (2025)
- Source: arXiv | http://arxiv.org/abs/2504.06156v2
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Sensing/control loop using tactile, force, or impedance signals.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions
- Variables treated as fixed: object geometry, task family, and controller interface
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences

## 85. Hydrosoft: Non-Holonomic Hydroelastic Models for Compliant Tactile Manipulation (2025)
- Source: arXiv | http://arxiv.org/abs/2509.13126v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Optimization over trajectories, contact modes, or continuous constraints.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift
- Variables treated as fixed: grasp taxonomy or candidate grasp set; simulator contact parameters
- Failure modes ignored: role-equivalent contacts that induce different mechanics
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools

## 86. Hand-centric Human-to-Robot Trajectory Transfer from Video Demonstrations via Open-World Contact Localization (2026)
- Source: arXiv | http://arxiv.org/abs/2606.10743v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Optimization over trajectories, contact modes, or continuous constraints.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions; language decompositions preserve physical contact preconditions
- Variables treated as fixed: grasp taxonomy or candidate grasp set; camera viewpoint and perceptual segmentation quality; prompted skill API and object labels
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering; plausible verbal plan that skips a necessary physical contact
- What it makes less novel: contact-mode planning and contact-rich control; LLM program/planner interfaces for robot manipulation
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences

## 87. Mag-VLA: Vision-Language-Action Model for Bimanual Magnetically Actuated Microrobot Manipulation (2026)
- Source: arXiv | http://arxiv.org/abs/2605.28486v1
- Problem claimed: Enable robots to select, grasp, design, or use tools for physical tasks.
- Actual mechanism introduced: Language-model or vision-language-model decomposition into robot actions.
- Hidden assumptions: tool function is stable across grasp, approach, and target geometry; contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions; language decompositions preserve physical contact preconditions
- Variables treated as fixed: camera viewpoint and perceptual segmentation quality; prompted skill API and object labels
- Failure modes ignored: role-equivalent contacts that induce different mechanics; grasp makes the functional end unreachable or reverses the required contact side; out-of-distribution tool compositions that require unseen role ordering; plausible verbal plan that skips a necessary physical contact
- What it makes less novel: contact-mode planning and contact-rich control; tool-use transfer, task-oriented grasping, and tool design; LLM program/planner interfaces for robot manipulation
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; generalization from tool parts to ordered tool-target-environment contact productions

## 88. SECOND-Grasp: Semantic Contact-guided Dexterous Grasping (2026)
- Source: arXiv | http://arxiv.org/abs/2605.13117v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Language-model or vision-language-model decomposition into robot actions.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions; language decompositions preserve physical contact preconditions
- Variables treated as fixed: grasp taxonomy or candidate grasp set; camera viewpoint and perceptual segmentation quality; prompted skill API and object labels
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering; plausible verbal plan that skips a necessary physical contact
- What it makes less novel: contact-mode planning and contact-rich control; LLM program/planner interfaces for robot manipulation
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences

## 89. FAVLA: A Force-Adaptive Fast-Slow VLA model for Contact-Rich Robotic Manipulation (2026)
- Source: arXiv | http://arxiv.org/abs/2602.23648v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Language-model or vision-language-model decomposition into robot actions.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; language decompositions preserve physical contact preconditions
- Variables treated as fixed: camera viewpoint and perceptual segmentation quality; predicate vocabulary and action library; prompted skill API and object labels
- Failure modes ignored: role-equivalent contacts that induce different mechanics; plausible verbal plan that skips a necessary physical contact
- What it makes less novel: contact-mode planning and contact-rich control; LLM program/planner interfaces for robot manipulation
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; mechanism-level error diagnosis instead of plan/no-plan output

## 90. Implicit Contact-Rich Manipulation Planning for a Manipulator with Insufficient Payload (2023)
- Source: arXiv | http://arxiv.org/abs/2302.13212v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Optimization over trajectories, contact modes, or continuous constraints.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift
- Variables treated as fixed: grasp taxonomy or candidate grasp set; simulator contact parameters; predicate vocabulary and action library
- Failure modes ignored: role-equivalent contacts that induce different mechanics
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; mechanism-level error diagnosis instead of plan/no-plan output

## 91. DexFuture: Hierarchical Future-State Visuomotor Targeting for Bimanual Dexterous Tool Use (2026)
- Source: arXiv | http://arxiv.org/abs/2606.05699v1
- Problem claimed: Enable robots to select, grasp, design, or use tools for physical tasks.
- Actual mechanism introduced: Optimization over trajectories, contact modes, or continuous constraints.
- Hidden assumptions: tool function is stable across grasp, approach, and target geometry; contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions
- Variables treated as fixed: predicate vocabulary and action library
- Failure modes ignored: role-equivalent contacts that induce different mechanics; grasp makes the functional end unreachable or reverses the required contact side; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: contact-mode planning and contact-rich control; tool-use transfer, task-oriented grasping, and tool design
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; generalization from tool parts to ordered tool-target-environment contact productions; mechanism-level error diagnosis instead of plan/no-plan output

## 92. ShapeGrasp: Simultaneous Visuo-Haptic Shape Completion and Grasping for Improved Robot Manipulation (2026)
- Source: arXiv | http://arxiv.org/abs/2605.02347v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Sensing/control loop using tactile, force, or impedance signals.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift
- Variables treated as fixed: grasp taxonomy or candidate grasp set; simulator contact parameters; predicate vocabulary and action library
- Failure modes ignored: role-equivalent contacts that induce different mechanics
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; mechanism-level error diagnosis instead of plan/no-plan output

## 93. A Humanoid Visual-Tactile-Action Dataset for Contact-Rich Manipulation (2025)
- Source: arXiv | http://arxiv.org/abs/2510.25725v2
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Optimization over trajectories, contact modes, or continuous constraints.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions
- Variables treated as fixed: object geometry, task family, and controller interface
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences

## 94. PolyTouch: A Robust Multi-Modal Tactile Sensor for Contact-rich Manipulation Using Tactile-Diffusion Policies (2025)
- Source: arXiv | http://arxiv.org/abs/2504.19341v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Sensing/control loop using tactile, force, or impedance signals.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions
- Variables treated as fixed: camera viewpoint and perceptual segmentation quality
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences

## 95. VibeCheck: Using Active Acoustic Tactile Sensing for Contact-Rich Manipulation (2025)
- Source: arXiv | http://arxiv.org/abs/2504.15535v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Sensing/control loop using tactile, force, or impedance signals.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions
- Variables treated as fixed: grasp taxonomy or candidate grasp set; simulator contact parameters
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences

## 96. CATCH-FORM-ACTer: Compliance-Aware Tactile Control and Hybrid Deformation Regulation-Based Action Transformer for Viscoelastic Object Manipulation (2025)
- Source: arXiv | http://arxiv.org/abs/2504.08232v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Optimization over trajectories, contact modes, or continuous constraints.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions
- Variables treated as fixed: predicate vocabulary and action library
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences; mechanism-level error diagnosis instead of plan/no-plan output

## 97. A Survey of Optimization-based Task and Motion Planning: From Classical To Learning Approaches (2024)
- Source: arXiv | http://arxiv.org/abs/2404.02817v5
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Optimization over trajectories, contact modes, or continuous constraints.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions; language decompositions preserve physical contact preconditions; predicates expose the contact roles needed by the continuous planner
- Variables treated as fixed: predicate vocabulary and action library; prompted skill API and object labels
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering; plausible verbal plan that skips a necessary physical contact
- What it makes less novel: contact-mode planning and contact-rich control; symbolic precondition/effect planning; LLM program/planner interfaces for robot manipulation
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences; mechanism-level error diagnosis instead of plan/no-plan output

## 98. TLA: Tactile-Language-Action Model for Contact-Rich Manipulation (2025)
- Source: arXiv | http://arxiv.org/abs/2503.08548v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Language-model or vision-language-model decomposition into robot actions.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift; training distribution covers the relevant contact compositions; language decompositions preserve physical contact preconditions
- Variables treated as fixed: camera viewpoint and perceptual segmentation quality; prompted skill API and object labels
- Failure modes ignored: role-equivalent contacts that induce different mechanics; out-of-distribution tool compositions that require unseen role ordering; plausible verbal plan that skips a necessary physical contact
- What it makes less novel: contact-mode planning and contact-rich control; LLM program/planner interfaces for robot manipulation
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools; distribution-free checks for impossible contact sequences

## 99. FAWAM: Force-Aware World Action Models for Closed-Loop Contact-Rich Manipulation (2026)
- Source: arXiv | http://arxiv.org/abs/2606.08555v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Optimization over trajectories, contact modes, or continuous constraints.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift
- Variables treated as fixed: camera viewpoint and perceptual segmentation quality
- Failure modes ignored: role-equivalent contacts that induce different mechanics
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools

## 100. Tactile-Proprioceptive Sensor Fusion for Contact Wrench Estimation in Whole-Body Physical Human-Robot Interaction (2026)
- Source: arXiv | http://arxiv.org/abs/2605.28412v1
- Problem claimed: Plan or control contact-rich manipulation under discontinuous mechanics.
- Actual mechanism introduced: Sensing/control loop using tactile, force, or impedance signals.
- Hidden assumptions: contact mode abstractions are available or can be searched without semantic role drift
- Variables treated as fixed: simulator contact parameters
- Failure modes ignored: role-equivalent contacts that induce different mechanics
- What it makes less novel: contact-mode planning and contact-rich control
- What it leaves open: a compact symbolic language for role-typed contact transitions across tools
