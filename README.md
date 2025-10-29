# 🌱 Soil Health Analysis using Feature Reduction in Machine Learning

## Overview
This project analyzes soil health data using feature reduction techniques like PCA and Decision Tree feature selection.
The goal is to identify key soil attributes influencing fertility and to build a Decision Support System (DSS) for crop/fertilizer recommendations.

## Tech Stack
- Python (main language)
- Jupyter Notebook / Google Colab
- Libraries: scikit-learn, pandas, numpy, matplotlib, seaborn, SHAP, Streamlit

## Folder Structure
data/
├── raw/ → Original datasets
└── processed/ → Cleaned datasets
notebooks/ → Jupyter/Colab notebooks
scripts/ → Python scripts for modeling
docs/ → Reports, presentations


## Team Roles
| Member | Role |
|--------|------|
| M1 | Workflow & Documentation |
| M2 | Data Collection & Cleaning |
| M3 | GitHub & Environment Setup |
| M4 | Preprocessing & Standardization |

## How to Run
1. Clone repo  
   ```bash
   git clone https://github.com/<your-username>/soil-health-feature-reduction-ml.git





## 🧠 Day 4 – Model Optimization, Comparison & Visualization

### 👩‍🔬 Member 1 – Model Optimization
- Performed hyperparameter tuning using GridSearchCV on Random Forest.
- Found best parameters and improved the model pipeline.
- Saved the optimized model as `optimized_random_forest.joblib`.

### 🧮 Member 2 – Model Comparison
- Compared base Random Forest vs Optimized Random Forest.
- Evaluated metrics: Accuracy, Precision, Recall, and F1-Score.
- Displayed results in tabular format.

### 📊 Member 3 – Model Visualization
- Visualized feature importance (top features affecting yield).
- Plotted confusion matrix for the optimized model.
- Generated performance classification report.

### 📈 Member 4 – Dashboard Visualization
- Compared model accuracy visually using bar charts.
- Created a combined dashboard for model metrics.
- Exported visuals to `/reports/figures/`.

### 📦 Outputs
- Optimized model saved: `models/optimized_random_forest.joblib`
- Figures saved:  
  - `feature_importance.png`  
  - `confusion_matrix.png`  
  - `model_accuracy_comparison.png`
