# Hierarchical Predicate Discovery

LOGGED: 12 June 2025

STATUS: In progress

## Idea:

Automatically discover hierarchical symbolic predicates during RL training. Start with basic predicates (color, shape) and learn compound ones (openable_door = door AND has_handle).

* Uses well-established clustering/association techniques
* Can fall back to manual predicate definition if auto-discovery fails
* Clear evaluation metrics (predicate usefulness, sample efficiency)

## Research Quality:

1. Novel Symbolic-RL Integration
    * **Unique Contribution**: Most RL systems use neural embeddings. This one discovers *interpretable symbolic abstractions*.
    * **Research Value**: Bridges symbolic AI and modern RL in a principled way.

2. Sophisticated Pattern Mining:
    * **Technical Improvement**: The pattern implemented uses constraint satisfcation + unification (typically found in theorem provers, not RL)
    * **SOTA**: Most work uses simple co-occurrence; this implementation uses *variable binding consistency* across complex logical expressions.

3. **Statistical Validation Pipeline**:
    * **Research Rigor**: Support + confidence thresholds prevent spurious discoveries
    * **Novelty**: Most symbolic systems are hand-coded; This one learns predicates from experience data

## Future Work/To-Do List:

1. **Emperical Validation**:
    * Need: Comparison with baselines on standard benchmarks
    * Missing: Preformance metrics, learning curves, generalization tests

2. **Theoretical Foundations**:
    * Need: Formal analysis of convergence, sample complexity
    * Missing: Proofs about when/why the algorithm works

3. **Scalability Demonstration**:
    * Need: Evaluation on complex domains (not just simple toy games)
    * Missing: Performance on domains with 100+ predicates