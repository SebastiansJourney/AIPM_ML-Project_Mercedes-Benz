# 🏎️ Mercedes-Benz Greener Manufacturing: Time-to-Test Prediction

> A team ML project applying end-to-end product management methodology to a real Kaggle regression challenge — predicting vehicle test bench duration to reduce manufacturing bottlenecks and emissions.

[![Python](https://img.shields.io/badge/Python-3.11.3-3776AB?logo=python&logoColor=white)](https://python.org)
[![scikit-learn](https://img.shields.io/badge/ML-scikit--learn-F7931E?logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![XGBoost](https://img.shields.io/badge/ML-XGBoost-189fdd)](https://xgboost.readthedocs.io)
[![Kaggle](https://img.shields.io/badge/Data-Kaggle-20BEFF?logo=kaggle)](https://www.kaggle.com/c/mercedes-benz-greener-manufacturing)

---

## 1. Non-Technical Executive Summary

In automotive manufacturing, the final testing phase is a critical but costly bottleneck. Every minute a premium vehicle spends on the test bench accumulates operational expense (OpEx) and delays revenue realization.

This project builds a regression model to predict test bench duration for any given vehicle configuration. A high-performing model enables **Just-in-Time (JIT) resource allocation** — reducing idle time of expensive testing machinery and labor — while directly supporting sustainability goals by minimising the carbon emissions associated with extended testing cycles.

**This repo documents not just the ML work, but the full PM process behind it** — from PRD and OKR mapping through model experimentation to post-launch planning.

---

## 2. Product Requirements Document (PRD)

| Component | Definition |
|---|---|
| **Problem Statement** | Testing cars takes variable time, creating bottlenecks in production and increasing emissions |
| **User Persona** | Production Planning Manager — needs accurate forecasts to schedule workers and test benches efficiently |
| **In-Scope** | Predicting testing time (seconds) for anonymized vehicle configurations |
| **Out-of-Scope** | Predicting mechanical failures or optimizing car features themselves |
| **Constraints** | Data is fully anonymized; computation must be efficient enough for batch prediction |

---

## 3. OKR & KPI Mapping

**Primary Business Objective (OKR):** Reduce average vehicle testing dwell time to improve inventory turnover.

**Supporting KPIs:**

| KPI | Financial Driver |
|---|---|
| Cars tested per hour (throughput) | Revenue velocity |
| % of tests completed within predicted window | Labor utilization |
| OpEx per unit tested | Cost efficiency |

**ML-to-Product Metric Chain:**
```
Model R² increases
    → Prediction variance decreases
    → Scheduling buffers can be tightened
    → OpEx per unit decreases
```

---

## 4. Data Understanding & EDA

**Data Source:** [Kaggle — Mercedes-Benz Greener Manufacturing](https://www.kaggle.com/c/mercedes-benz-greener-manufacturing)

The dataset contains anonymized vehicle configurations (binary and categorical features) mapped to test bench duration in seconds.

**Key characteristics:**
- Target variable (`y`): continuous, right-skewed distribution — most cars test quickly, with a long tail of complex configurations
- High binary feature sparsity — many features are rarely active across the dataset
- No feature labels available due to full anonymization, limiting interpretability

**Data risk:** Because features are fully anonymized, we cannot validate what each column represents (e.g. is Feature X a safety sensor or a trim option?). This limits explainability but does not affect predictive performance.

See `notebooks/01_EDA.ipynb` for full analysis.

---

## 5. ML Framing & Metrics

**Problem type:** Supervised regression

**Primary metric:** R² (Coefficient of Determination)
> R² represents the proportion of variance in test bench time explained by the model — directly correlating to how much scheduling uncertainty is removed.

**Baseline:** Mean testing time (predicting the average for every car) → R² = 0.00

**Key trade-off:** Accuracy over interpretability. Since features are already anonymized, there is no benefit to using interpretable models — we optimise purely for predictive performance.

---

## 6. Model Experiment Log

| Experiment | Model | Notes | R² |
|---|---|---|---|
| 1.0 | Baseline (mean) | Predict average for all cars | 0.00 |
| 1.1 | Linear Regression | Initial benchmark, assumes linear relationships | TBD |
| 1.2 | Random Forest | Handles non-linearity, robust to outliers | TBD |
| 1.3 | XGBoost | Gradient boosting, expected best performer | TBD |

> **Note:** Model experiments are in progress. Results will be updated as experiments complete. See `notebooks/` for current state.

---

## 7. Ethical, Risk & Failure Analysis

**Bias & Fairness Risk:**
The model might systematically overestimate time for specific car configurations, leading to deprioritization in the production queue. Mitigation: analyse residual errors across different feature clusters to detect systematic bias.

**Key Failure Scenario:**

| Scenario | Impact | Mitigation |
|---|---|---|
| Model predicts 50s, actual is 200s | Scheduling conflict, assembly line backup | Add buffer time based on prediction confidence intervals |
| Model degrades over time (data drift) | Silent performance drop | Monitor R² weekly, retrain if it drops below 0.50 for two consecutive weeks |

---

## 8. Post-Launch Plan

**Monitoring trigger:** Retrain if R² drops below 0.50 for two consecutive weeks.

**Rollback strategy:** If inference latency exceeds 100ms or errors spike, revert immediately to the mean baseline model.

**Next iteration:** Request non-anonymized metadata for outlier cars (test time >200s) to improve model interpretability and edge case handling.

---

## 9. Repository Structure

```
AIPM_ML-Project_Mercedes-Benz/
├── data/                  # Raw and processed data
├── notebooks/
│   └── 01_EDA.ipynb       # Data understanding & feasibility analysis
├── src/                   # Modular source code
├── requirements.txt
└── README.md
```

---

## 10. Project Background

Built as part of the **AIPM Bootcamp** (neuefische, Cohort 1 · 2025/26) — a team project of three, structured as a real product initiative rather than a pure ML exercise.

The goal was to apply full PM methodology to an ML project: writing a PRD, defining OKRs and KPIs before touching any data, mapping model metrics to business outcomes, and planning for post-launch monitoring and failure scenarios.

The Kaggle dataset was chosen because its anonymization mirrors real-world constraints — where data science teams often work with features they cannot fully explain to stakeholders.

---

## Team

Built with teammates from the AIPM Bootcamp Cohort 1 · neuefische 2025/26

**Sebastian** (PM Lead & ML)
[GitHub](https://github.com/SebastiansJourney) · [LinkedIn](https://www.linkedin.com/in/sebastian-plum-aipm)
