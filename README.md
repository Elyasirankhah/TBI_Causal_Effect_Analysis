# TBI Causal Effect Analysis

This repository contains analysis of the **causal effect of surgical interventions (Craniotomy/Craniectomy)** on various discharge outcomes in patients with Traumatic Brain Injury (TBI) in the TBIMS Dataset.

We evaluate the **Average Treatment Effect (ATE)** and **Average Treatment Effect on the Treated (ATT)** using stratified estimation methods. We also perform t-tests to assess statistical differences between treated and control groups.

## 📊 Analysis Summary

| Outcome        | ATE Estimate | ATT Estimate | T-Test (p-value) |
|----------------|--------------|--------------|------------------|
| FIMCompD       | -1.27        | -2.49        | 0.2522           |
| FIMMemD        | -1.14        | -2.12        | 0.4637           |
| FIMProbSlvD    | -1.21        | -2.41        | 0.3727           |
| FIMExpressD    | -1.39        | -2.49        | 0.3008           |
| FIMSocialD     | -1.11        | -2.26        | 0.2866           |

> **Note:** All effects are negative, suggesting that surgery may be associated with *lower* discharge scores, although none of the t-tests indicate statistical significance (p > 0.05).

---

## 📁 Contents

- `Final_Analysis.ipynb`: Full notebook with all data processing, stratification, ATE, ATT, and t-test computations.
- `severity_control_processed.csv`: Cleaned dataset used for the analysis.
  
## 📚 Methods

- Stratified groupings based on key confounders: `SexF`, `SCI`, `Hypertension`
- ATT: Calculated using weights from treated group only (GCS < 8)
- ATE: Computed over the full population (GCS ≤ 20)
- T-test: Welch’s test (unequal variance) between treated and control outcomes

## 📌 Requirements

- Python ≥ 3.8
- pandas
- numpy
- seaborn
- matplotlib
- scipy

Install dependencies using:

```bash
pip install -r requirements.txt
