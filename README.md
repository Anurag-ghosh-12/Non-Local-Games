# Non-Local Games and Quantum Advantage

## Overview

This repository contains the computational analysis, datasets, and visualizations developed for research on **biased-input non-local games and quantum advantage**.

Non-local games provide a framework for studying the difference between classical and quantum correlations. In these games, spatially separated players respond to questions without communicating after the game begins. Classical players are restricted to classical strategies, while quantum players can use shared entanglement to produce correlations that may achieve higher winning probabilities.

The main objective of this work is to systematically compare **classical and quantum strategies across different non-local games and input probability ranges**. The analysis investigates how the winning probabilities change with the input distribution and identifies the probability ranges where quantum strategies provide an advantage.

This repository includes:

* Python scripts for evaluating the relevant game equations and computing classical strategy values.
* Numerical data used in this work.
* Detailed strategy-wise analysis comparing classical strategies with quantum performance.
* Plots illustrating quantum success probabilities and quantum advantage across different games and probability ranges.

---

## Repository Structure

```text
.
├── code/
│   ├── classical_win_compute_scripts/
│   │   ├── 10win_3331.py
│   │   ├── 5win_2111.py
│   │   ├── 6win_3111.py
│   │   ├── 7win_2221.py
│   │   ├── 8win_2222.py
│   │   ├── 8win_3311.py
│   │   └── 9win_3321.py
│   │
│   └── plotting_scripts/
│       ├── 10win_3331_finalplot.py
│       ├── 5win_2111_finalplot.py
│       ├── 6win_3111_finalplot.py
│       ├── 7win_2221_finalplot.py
│       ├── 8win_2222_finalplot.py
│       ├── 8win_3311_finalplot.py
│       ├── 9win_3321_finalplot.py
│       ├── MaxQuantumSuccessprob_0.4to0.6_plot.py
│       ├── Quantum Advantageinrangepequals0.45to0.55).py
│       ├── Quantum_adv_plotter.py
│       ├── advatpequals0.5forallgames_plot.py
│       └── quantum_advantage_obtained_inp0.3to0.7_plot.py
│
├── plots/
│   ├── quantum_success_and_advantage_plots/
│   │   ├── MaxQuantumSuccessProb_forall2prtygames_Plot.png
│   │   └── quantumadvantage_all2prtygames.png
│   │
│   └── quantvsclassical_plots/
│       ├── 10win(3331).png
│       ├── 5win(2111).png
│       ├── 6win(3111).png
│       ├── 7win(2221).png
│       ├── 8win(2222-CHSH).png
│       ├── 8win(3221).png
│       ├── 9win(3321).png
│       └── max_quantum_adv_atp_equals_0.5.png
│
├── tables/
│   ├── classical_strategy_values/
│   │   ├── strategy_values_10win.csv
│   │   ├── strategy_values_5win.csv
│   │   ├── strategy_values_6win.csv
│   │   ├── strategy_values_7win.csv
│   │   ├── strategy_values_8win(3+3+1+1).csv
│   │   ├── strategy_values_8winCHSH.csv
│   │   └── strategy_values_9win.csv
│   │
│   ├── quantum_strategy_values/
│   │   ├── data2111.txt
│   │   ├── data2221.txt
│   │   ├── data2222.txt
│   │   ├── data3111.txt
│   │   ├── data3221.txt
│   │   ├── data3321.txt
│   │   └── data3331.txt
│   │
│   └── quantum_strategy_values(p0.4to0.6,incr0.02)/
│       ├── data2111(adv).txt
│       ├── data2221(adv).txt
│       ├── data2222(adv).txt
│       ├── data3111(adv).txt
│       ├── data3221(adv).txt
│       ├── data3321(adv).txt
│       └── data3331(adv).txt
│
├── all_classical_strategy_analysis.xlsx
├── quantum_advantage_analysis.xlsx
└── README.md
```

---

# Code

The `code/` directory contains the scripts used for the computational analysis and generation of the plots.

## Classical Winning Probability Computation

The `classical_win_compute_scripts/` directory contains Python scripts used to evaluate the relevant game equations and compute the winning probabilities of the possible classical strategies for each considered non-local game.

The games considered in this analysis include:

* 5-win game `(2111)`
* 6-win game `(3111)`
* 7-win game `(2221)`
* 8-win game `(2222)`
* 8-win game `(3311)`
* 9-win game `(3321)`
* 10-win game `(3331)`
## Plotting Scripts

The `plotting_scripts/` directory contains the Python scripts used to generate the figures from the classical and quantum strategy data.

The scripts generate plots for:

* Comparison of classical and quantum winning probabilities.
* Quantum advantage across different probability ranges.
* Maximum quantum success probabilities.
* Quantum advantage around (p = 0.5).
* Quantum advantage over selected probability intervals.
* Comparative analysis across all considered games.

These scripts use the computed and collected data stored in the `tables/` directory.

---

# Tables and Data

The `tables/` directory contains the numerical data used throughout the analysis.

## Classical Strategy Values

The `classical_strategy_values/` directory contains the computed winning probabilities of the classical strategies for each considered game.

## Quantum Strategy Values

The `quantum_strategy_values/` directory contains the quantum strategy values used for the considered non-local games.

## Detailed Quantum Strategy Values

The `quantum_strategy_values(p0.4to0.6,incr0.02)/` directory contains quantum strategy values for the probability range from (p = 0.4) to (p = 0.6), with an increment of `0.02`.

This dataset provides a more detailed view of quantum performance within this probability range and is used for the corresponding detailed quantum advantage analysis.

---

# Plots

The `plots/` directory contains the visualizations generated from the computational analysis.

## Quantum Success and Advantage Plots

The `quantum_success_and_advantage_plots/` directory contains plots showing:

* The maximum quantum success probabilities across the considered two-party games.
* The variation of quantum advantage across the different games in a particular range.

## Quantum vs Classical Plots

The `quantvsclassical_plots/` directory contains game-wise comparisons between classical and quantum strategies.

These plots show how the winning probabilities of the classical and quantum strategies vary with the input probability. They help visualize the regions where:

* The quantum strategy outperforms the classical strategy.
* Classical and quantum strategies have similar performance.
* A classical strategy may outperform the quantum strategy.

The directory also contains a plot comparing the maximum quantum advantage across the games at (p = 0.5).

---

# Detailed Classical Strategy Analysis

## `all_classical_strategy_analysis.xlsx`

This is one of the main analysis files in the repository.

It contains a detailed strategy-wise analysis of the classical strategies considered for each non-local game. Rather than only comparing the best classical winning probability with the quantum winning probability, this file examines the performance of **individual classical strategies** across different input probability ranges.

The analysis allows us to study:

* How each classical strategy performs as the input probability changes.
* Which classical strategy performs best in different probability ranges.
* How individual classical strategies perform compared with the quantum strategy.
* Whether any classical strategy matches or outperforms the quantum strategy.
* The probability ranges where a classical strategy outperforms the quantum strategy, if such ranges exist.
* The probability ranges where the quantum strategy outperforms all considered classical strategies.

This file provides a detailed view of the transition in strategy performance as the input probability changes and is an important part of the overall classical-versus-quantum comparison.

---

# Contributors

* **Anurag Ghosh**
* **Jyotirmoy Basak**

Research on **Two-party Nonlocal Games for Biased Inputs**.
