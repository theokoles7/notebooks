# Symbolic Attention RL
12 June 2025

A novel reinforcement learning approach that combines symbolic reasoning with attention mechanisms for improved generalization and interpretability.

## Overview

This repository implements Symbolic Attention Mechanisms - a new paradigm where RL agents learn to attend to objects and relationships using symbolic predicates rather than raw features. Instead of learning "attend to pixels at location (x,y)", agents learn logical attention patterns like "attend to objects where color(X, red) AND movable(X)".

## Key Features

* ### Symbolic Attention: 
    Attention mechanisms that operate over logical predicates

* ### Differentiable Logic:
    Gradient-based learning of symbolic attention patterns

* ### Compositional Generalization:
    Learned attention transfers across tasks with different objects

* ### Interpretable Decisions:
    Transparent reasoning about what the agent is focusing on

## Research Contribution

This work addresses a gap in neuro-symbolic reinforcement learning by introducing attention mechanisms that can:

* Learn logical attention patterns from experience
* Generalize symbolic attention rules to new scenarios
* Provide interpretable explanations for agent behavior
* Improve sample efficiency on structured tasks

## Example Use Case

In a blocksworld environment, traditional RL might learn task-specific pixel patterns. Our approach learns reusable symbolic attention:

* Task: "Collect red blocks" → Learns to attend where `color(X, red) AND movable(X)`
* New task: "Collect blue blocks" → Immediately generalizes to `color(X, blue) AND movable(X)`