# Mercedes-Benz Greener Manufacturing: Time-to-Test Prediction

![Status](https://img.shields.io/badge/Status-In_Progress-yellow) ![Python](https://img.shields.io/badge/Python-3.x-blue) ![Type](https://img.shields.io/badge/ML-Regression-green)

## 1. Non-Technical Executive Summary
**Project Context & Financial Impact**
In the automotive industry, the final testing phase is a critical but costly bottleneck. Every minute a premium vehicle spends on the test bench represents a direct accumulation of operational expense (OpEx) and a delay in revenue realization. Mercedes-Benz has launched this initiative to streamline that process. By leveraging an anonymized dataset representing different permutation of car features, we aim to accurately predict the testing duration (`y`) for any given vehicle configuration.

**Objectives & Value Proposition**
The primary objective of this project is to build a regression model that minimizes the error in predicting test bench time. From a financial perspective, a high-performing model allows for **Just-In-Time (JIT) resource allocation**—reducing the idle time of expensive testing machinery and labor. Furthermore, optimizing this process directly supports sustainability goals by reducing the carbon emissions associated with extended testing cycles, aligning technical efficiency with corporate social responsibility (CSR) targets.

---

## 2. Product Requirements Document (PRD)
*Defining the "Why" and "Who" before the "How".*

| Component | Definition |
| :--- | :--- |
| **Problem Statement** | Testing cars takes variable time, creating bottlenecks in production and increasing emissions. |
| **User Persona** | **Production Planning Manager:** Needs accurate forecasts to schedule workers and test benches efficiently to minimize downtime. |
| **In-Scope** | Predicting testing time (seconds) for anonymized vehicle configurations. |
| **Out-of-Scope** | Predicting mechanical failures or optimizing the car features themselves. |
| **Constraints** | Data is fully anonymized; computation must be efficient enough for batch prediction. |

---

## 3. KPI & OKR Mapping
*Bridging Model Performance to Business Success.*

* **Primary Business Objective (OKR):** Reduce average vehicle testing dwell time by X% in Q4 to improve inventory turnover.
* **Supporting KPIs:**
    * **Throughput:** Cars tested per hour (Financial Driver: Revenue Velocity).
    * **Scheduling Accuracy:** % of tests completed within the predicted time window (Financial Driver: Labor Utilization).
* **ML-to-Product Metric Mapping:**
    * *If Model R² increases* $\rightarrow$ *Variance in prediction decreases* $\rightarrow$ *Scheduling buffers can be tightened* $\rightarrow$ *OpEx per unit decreases.*

---

## 4. Data Understanding & EDA Summary
*See `notebooks/01_EDA.ipynb` for full analysis.*

* **Data Sources:** Kaggle Competition Dataset (anonymized car features).
* **Key Insights:**
    * [TODO: Insert insight on Target Variable Distribution from EDA]
    * [TODO: Insert insight on Binary Feature Sparsity from EDA]
* **Data Gaps & Risks:**
    * **Anonymity:** We cannot validate feature meaning (e.g., is "Feature X" a safety sensor?), limiting interpretability.
    * **Feasibility Assessment:** [TODO: GO/NO-GO Decision based on signal-to-noise ratio].

---

## 5. ML Framing & Metrics
* **Problem Type:** Regression (Supervised Learning).
* **Primary Evaluation Metric:** Coefficient of Determination ($R^2$).
    * *Justification:* $R^2$ represents the proportion of variance in testing time explained by our model, directly correlating to how much "uncertainty" we remove for the scheduler.
* **Baseline:** Mean Testing Time (Predicting the average for every car).
* **Key Trade-offs:**
    * **Accuracy vs. Interpretability:** We prioritize Accuracy ($R^2$) over interpretability since features are already anonymized.

---

## 6. Model Experiment Log
*Tracking iterative improvements.*

| Experiment | Change / Hypothesis | Result ($R^2$) | Decision |
| :--- | :--- | :--- | :--- |
| **1.0 Baseline** | Calculate mean of train set | 0.00 | **Benchmark** |
| **1.1 XGBoost** | [TODO: Describe initial hyperparams] | [TODO] | [TODO: Keep/Discard] |
| **1.2 Feature Eng**| [TODO: e.g., PCA decomposition] | [TODO] | [TODO] |

---

## 7. Ethical, Risk & Failure Analysis
*What happens when the model is wrong?*

* **Bias & Fairness:**
    * *Risk:* The model might systematically overestimate time for specific car configurations (e.g., budget models), leading to deprioritization in the queue.
    * *Mitigation:* Analyze residual errors across different feature clusters.
* **Failure Modes & Edge Cases:**
    * *Scenario:* Model predicts 50s, actual test takes 200s.
    * *Impact:* Scheduling conflict; assembly line backup.
    * *Mitigation Strategy:* Implement a "buffer time" based on prediction confidence intervals.

---

## 8. Post-Launch Plan & Iteration Roadmap
*Lifecycle Management.*

* **Monitoring Trigger:** Retrain model if $R^2$ drops below 0.50 for two consecutive weeks.
* **Rollback Strategy:** If inference latency exceeds 100ms or errors spike, revert immediately to the **Mean Baseline** model.
* **Next Data to Collect:** Request non-anonymized metadata for "outlier" cars that take >200s to test.

---

## 9. Repository Structure

```text
├── data/               # Raw and processed data
├── notebooks/          # Analysis and Prototyping
│   └── 01_EDA.ipynb    # Data Understanding & Feasibility
├── src/                # Modular code
├── README.md           # Product & Technical Documentation
└── requirements.txt    # Dependencies