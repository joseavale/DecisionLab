# DecisionLab

**A Python-based framework for simulation, optimisation, and decision-making under uncertainty.**

## Overview

DecisionLab is an independent project exploring how mathematical models can support optimal decisions in dynamic systems, particularly when information is incomplete and outcomes are uncertain.

The initial application is Formula 1 race strategy, where the objective is to determine optimal pit-stop timing based on tyre performance, degradation, and operational constraints.

Although motorsport provides the starting environment, the underlying concepts are applicable to broader problems in operations research, quantitative finance, energy systems, and decision science.

## Project Objectives

The project is being developed incrementally, progressing from simple deterministic models towards more sophisticated decision-making systems.

Key areas of exploration include:

- **Optimisation:** Identifying optimal decisions under defined constraints.
- **Sensitivity Analysis:** Understanding how model assumptions influence optimal decisions.
- **Stochastic Simulation:** Modelling uncertainty and evaluating distributions of possible outcomes.
- **Probabilistic Modelling:** Estimating uncertain system parameters from observations.
- **Adaptive Decision-Making:** Updating strategies as new information becomes available.

## Current Implementation

**Version 1 — Deterministic Race Strategy Optimisation**

The current model:

- Calculates cumulative stint times using simplified tyre performance and degradation models.
- Evaluates possible pit-stop laps for a fixed race distance and mandatory single stop.
- Identifies the strategy that minimises total predicted race time.

## Development Roadmap

- [x] Deterministic race-time model
- [x] Exhaustive pit-stop optimisation
- [ ] Parameter sensitivity analysis
- [ ] Stochastic performance modelling
- [ ] Monte Carlo strategy evaluation
- [ ] Decision-making under uncertainty
- [ ] Parameter estimation from observations
- [ ] Adaptive strategy optimisation
- [ ] Multi-agent and resource-constrained decision problems

## Technologies

- Python
- NumPy, SciPy, Pandas and Matplotlib (as required during development)
- Git and GitHub

## Long-Term Vision

To develop an extensible decision-making framework capable of modelling complex systems, evaluating alternative strategies, and supporting robust decisions under uncertainty.

The emphasis is on mathematical understanding, model validation, and optimisation methodology rather than graphical interfaces or application development.
