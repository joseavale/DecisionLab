# DecisionLab

A Python-based project exploring mathematical optimisation, machine learning, simulation, and decision-making under uncertainty.

## Overview

DecisionLab is an independent project focused on formulating, solving, and analysing decision problems using techniques from Operations Research, Decision Science, Machine Learning, and Mathematical Optimisation.

The initial application is Formula 1 race strategy, where decisions such as pit-stop timing must account for competing performance characteristics, operational constraints, and eventually uncertainty.

While motorsport provides an intuitive starting point, the project’s emphasis is on developing transferable mathematical and computational methods applicable to logistics, energy systems, resource allocation, financial modelling, and other optimisation problems.

## Project Objectives

The project is developed incrementally, with an emphasis on mathematical understanding, practical implementation, and reproducible analysis.

Its main objectives are to:

* Mathematical Optimisation: Formulate decision problems using objective functions, decision variables, and constraints.
* Data Analysis & SQL: Store, retrieve, and analyse experimental and simulation data.
* Machine Learning: Develop predictive models and investigate how predictions can inform optimal decisions.
* Sensitivity Analysis: Understand how changes in assumptions and model parameters influence optimal solutions.
* Stochastic Simulation: Model uncertainty and evaluate distributions of possible outcomes.
* Robust Decision-Making: Explore strategies that balance expected performance, risk, and operational constraints.
* Adaptive Optimisation: Update model estimates and decisions as new information becomes available.

## Current Implementation

Version 1 — Deterministic Race Strategy Optimisation

The initial model considers a race with two tyre compounds and one mandatory pit stop.

It includes:

* Simplified tyre performance and degradation models.
* Calculation of cumulative stint and race times.
* Exhaustive evaluation of candidate pit-stop laps.
* Identification of the strategy minimising predicted total race time.

This provides a baseline against which future optimisation methods can be compared.

## Development Roadmap

### Phase 1 — Deterministic Optimisation & SQL

* [x]	Develop deterministic race-time model
* [x]	Implement exhaustive search for optimal pit-stop timing
* [ ]	Parameterise tyre performance and race configuration
* [ ]	Conduct systematic sensitivity analysis
* [ ]	Store and query experimental results using SQLite and SQL

### Phase 2 — Mathematical Programming

* [ ]	Introduce additional decision variables and operational constraints
* [ ]	Formulate optimisation problems mathematically
* [ ]	Implement solver-based optimisation using Pyomo and HiGHS
* [ ]	Compare solver results against baseline algorithms
* [ ]	Evaluate computational performance and solution quality

### Phase 3 — Machine Learning & Predictive Modelling

* [ ]	Generate and analyse historical simulation datasets
* [ ]	Develop supervised learning models using scikit-learn
* [ ]	Compare Linear Regression, Random Forests, and Gradient Boosting
* [ ]	Evaluate predictive accuracy using appropriate validation methods
* [ ]	Explore uncertainty estimation using Gaussian Process Regression
* [ ]	Integrate ML predictions into optimisation models
* [ ]	Assess how prediction errors affect decision quality

### Phase 4 — Optimisation Under Uncertainty

* [ ]	Introduce stochastic performance models
* [ ]	Implement Monte Carlo simulation
* [ ]	Evaluate strategies across multiple scenarios
* [ ]	Explore stochastic and robust optimisation
* [ ]	Investigate the value of additional information

### Phase 5 — Adaptive and Advanced Decision-Making

* [ ]	Estimate uncertain model parameters from observed data
* [ ]	Update model estimates using incoming observations
* [ ]	Re-optimise decisions as new information becomes available
* [ ]	Explore sequential and multi-stage optimisation
* [ ]	Extend the framework to more complex resource allocation and competitive decision problems

The roadmap is indicative and will evolve as the project develops.

## Technology Stack

### Currently in use

* Python
* Git and GitHub

### Planned

* SQLite / SQL — experimental data storage, querying, and analysis
* Pyomo — mathematical optimisation modelling
* HiGHS — linear and mixed-integer optimisation
* scikit-learn — supervised learning and predictive modelling
* NumPy — numerical computation
* Pandas — data processing and analysis
* Matplotlib — visualisation and sensitivity studies

Additional libraries and tools may be introduced as the modelling requirements evolve.

## Methodology

Development follows an iterative approach:

1. Define the problem: Identify decision variables, objectives, constraints, and assumptions.
2. Build a baseline: Implement the simplest method capable of solving the problem.
3. Validate: Check model behaviour, predictions, and solution correctness.
4. Experiment: Investigate sensitivity to model parameters and uncertainty.
5. Improve: Introduce machine learning and advanced optimisation methods where justified.
6. Compare: Evaluate approaches in terms of predictive accuracy, solution quality, robustness, and computational performance.

The intention is to prioritise sound mathematical modelling and experimental rigour over unnecessary software complexity.

## Long-Term Vision

To develop a reproducible Python framework for investigating increasingly complex decision problems, integrating data analysis, predictive modelling, simulation, and mathematical optimisation.

The long-term focus is on understanding how to make effective decisions in systems involving uncertainty, competing objectives, and operational constraints.

Formula 1 strategy serves as the initial application rather than the intended limitation of the project.

## Project Status

Active development — early stage.

The deterministic optimisation baseline is implemented.

Current development priorities are:

* Parameter sensitivity analysis
* SQL integration
* Mathematical programming and solver-based optimisation

Future development will introduce machine learning, uncertainty quantification, and adaptive decision-making.