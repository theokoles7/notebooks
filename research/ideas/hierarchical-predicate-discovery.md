# Hierarchical Predicate Discovery

12 June 2025

## Idea:

Automatically discover hierarchical symbolic predicates during RL training. Start with basic predicates (color, shape) and learn compound ones (openable_door = door AND has_handle).

* Uses well-established clustering/association techniques
* Can fall back to manual predicate definition if auto-discovery fails
* Clear evaluation metrics (predicate usefulness, sample efficiency)