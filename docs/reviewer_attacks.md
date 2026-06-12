# Reviewer Attacks

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
   - Correct. The method assumes typed contact predicates are available from perception/control modules. The v2 perception-noise stress now quantifies this boundary: grammar F1 falls from 1.000 clean to 0.889 at 10% observed-predicate corruption and 0.778 at 20%.
7. **The theorem is tautological.**
   - It is conditional, but useful as an audit criterion: any claimed production must state the transition relation it preserves.
8. **Baselines are intentionally disadvantaged.**
   - They are stress tests of specific assumptions, not state-of-the-art systems. The paper must say this plainly.
9. **Grammar may explode combinatorially.**
   - The paper should report bounded-depth enumeration and discuss pruning by typed roles.
10. **Real tools deform, slip, and break.**
   - The simulator includes a small fragility/compliance gate only as a placeholder. Real contact physics remains a major weakness.
11. **The perfect symbolic observation assumption hides the hard part.**
   - Fair. The paper now states this directly and reports a corruption audit over observed features, side access, brace availability, fragility, length, and stiffness. The claim is representation under reliable predicates, not raw-perception robustness.
