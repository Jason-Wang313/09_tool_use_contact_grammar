# Hostile Reviewer Response

We agree that the current paper should not be read as a real-robot tool-use system. Its contribution is narrower: contact-role production rules expose the mechanical preconditions that static affordance labels and unordered contact sets can hide.

The strongest empirical result is in the controlled contact world, where the full grammar obtains F1 1.000 and false positive rate 0.000, while unordered contacts obtain F1 0.706 with false positive rate 0.345 and static affordances obtain F1 0.647 with false positive rate 0.427. The ablations are also diagnostic: removing specific production gates creates the expected false positives.

The main weakness is the assumed symbolic observation layer. In v2 we added a perception-noise stress that corrupts observed features, side access, brace availability, fragility, length, and stiffness before grammar planning while keeping oracle labels fixed. Grammar F1 is 0.973 at 2% noise, 0.935 at 5%, 0.889 at 10%, and 0.778 at 20%. This makes the boundary explicit: the claim is about representation under reliable typed predicates, not robust raw perception.

The paper should therefore be judged as a mechanism and falsification protocol. A stronger version would learn productions or predicates from tactile/vision data, connect them to contact-implicit controllers, and test on real tools under adversarial support, side-access, and compliance changes.
