# Causal Inference Framework Roadmap

7 June 2025

## 1. Causal Traces for Counterfactual Reasoning

Learning Counterfactual Action Traces in Neuro-Symbolic Reinforcement Learning

* ### Contribution:

    * Propose a causal trace module that logs "action → outcome" sequences as symbolic causal graphs.

    * Use these traces to simulate counterfactual rollouts ("what would’ve happened if...") during planning or training.

* ### Novelty:

    * First to combine counterfactual causal reasoning with symbolic abstraction in RL.

    * Improves both generalization and explanation.

## 2. Discovering Causal Programs from RL Interaction

Learning Structured Causal Programs from Reinforcement Learning Signals

* ### Contribution:

    * Propose a method for learning symbolic causal programs (e.g., rules like IF red_ball_left THEN GoLeft) from interaction.

    * Trains a hybrid neural-symbolic agent that extracts programs over time.

* ### Novelty:

    * Learns symbolic rules-as-programs through environment interactions instead of language supervision.

    * Bridges program induction and causal RL.

## 3. Causal Policy Distillation

Distilling Causal Abstractions from Black-Box Policies

* ### Contribution:

    * Train a black-box policy (e.g., PPO or a transformer agent), then extract symbolic causal graphs from observed transitions.

    * Use these graphs to train smaller/faster generalizable agents.

* ### Novelty:

    * Distillation of causal abstractions from opaque agents — creates a bridge between high-capacity and interpretable agents.

## 4. Unified Causal NSRL Framework

Toward a Unified Causal Inference Framework for Neuro-Symbolic Reinforcement Learning

* ### Contribution:

    Integrate prior modules: symbolic causal representation, counterfactual reasoning, causal policy learning, and generalization.

    Present the full causal NSRL agent.

* ### Novelty:

    Proposes a holistic system that systematically addresses representation, learning, reasoning, generalization, and explanation — grounded in causal theory.