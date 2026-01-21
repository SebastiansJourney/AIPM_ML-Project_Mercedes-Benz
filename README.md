# Mercedes-Benz Greener Manufacturing: Test Time Prediction

## 🎯 Business Goal
Mercedes-Benz focuses on safety and reliability, requiring every vehicle to pass rigorous test bench checks. However, this testing process is a bottleneck. 
**The Goal:** Optimize the testing system by predicting the time a car will spend on the test bench based on its configuration (features). Accurate predictions allow for better scheduling and reduced environmental impact.

## 📊 Data Overview
- **Source:** Kaggle (Mercedes-Benz Greener Manufacturing)
- **Input:** Anonymized features representing car configurations (binary and categorical).
- **Target (`y`):** Time (in seconds) the car spends on the test bench.
- **Key Insight:** The target distribution has a "long tail" of outliers (>130s) which represent the primary efficiency bottleneck.

## 📂 Project Structure
```text
├── data/               # Raw CSV files (Gitignored)
├── notebooks/          # Jupyter Notebooks for exploration
│   └── 01_EDA.ipynb    # Exploratory Data Analysis & Target visualization
├── src/                # Source code (Python package)
│   ├── __init__.py
│   └── data_loader.py  # Automated data cleaning pipeline
├── requirements.txt    # Python dependencies
├── setup.py            # Package installation setup
└── README.md           # Project documentation