# Reviewer Attacks

1. **Toy-world evidence is too weak.**
   - Fair for deployment claims. The paper is positioned as a mechanism and falsification protocol, now with a much larger deterministic stress suite rather than a small toy table.
2. **TAMP already has preconditions and effects.**
   - The boundary is that the predicates are contact-role productions over hand, tool, target, and environment, not generic object-state predicates. The paper makes this distinction central.
3. **Contact-mode planning already reasons about ordered contacts.**
   - True for continuous/hybrid planners. The novelty claim is not contact order alone, but a grammar-level representation that makes contact roles reusable and falsifiable across tools.
4. **Affordance work can include relations and sequences.**
   - The hostile set confirms this pressure. The paper avoids claiming affordances are always static; it claims that common affordance interfaces do not make production-level falsification central.
5. **The grammar library is hand-designed.**
   - Correct. The present contribution is representational and diagnostic. Learning productions is future work.
6. **No perception or control.**
   - Correct. The method assumes typed contact predicates are available from perception/control modules. The final predicate-noise suite quantifies this boundary: direct grammar F1 falls to 0.861 at 10% independent predicate noise and 0.642 at 30%.
7. **The targeted-probe fallback is too idealized.**
   - Correct. It is reported as an upper-bound symbolic diagnostic, not as a deployed sensor model.
8. **The theorem is tautological.**
   - It is conditional, but useful as an audit criterion: any claimed production must state the transition relation it preserves.
9. **Baselines are intentionally disadvantaged.**
   - They are assumption-isolation baselines, not state-of-the-art robot systems. The paper says this plainly and uses them to expose which representational variable is missing.
10. **Grammar may explode combinatorially.**
   - The paper reports bounded-depth enumeration and discusses pruning by typed roles.
11. **Real tools deform, slip, and break.**
   - The simulator includes fragility, friction, and compliance gates only as symbolic approximations. Real contact physics remains a major weakness and future-work boundary.
