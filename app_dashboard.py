import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# ------------------------------------------------------------
# 1️⃣ Page Setup
# ------------------------------------------------------------
st.set_page_config(page_title="Soil Health Model Dashboard", layout="wide")
st.title("🌾 Soil Health Model Performance Dashboard")

# ------------------------------------------------------------
# 2️⃣ Load Data
# ------------------------------------------------------------
try:
    corr = pd.read_csv("./data/processed/soil_correlation_matrix.csv", index_col=0)
    importance_df = pd.read_csv("./data/processed/soil_feature_importances.csv")
    model_report = open("./data/processed/model_accuracy_report.txt").read()
    st.success("✅ Data files loaded successfully!")
except Exception as e:
    st.error(f"❌ Error loading data: {e}")

# ------------------------------------------------------------
# 3️⃣ Display Model Performance
# ------------------------------------------------------------
st.header("📊 Model Accuracy Report")
st.text(model_report)

# ------------------------------------------------------------
# 4️⃣ Feature Importances Visualization
# ------------------------------------------------------------
st.header("🌿 Feature Importance")
fig, ax = plt.subplots()
sns.barplot(x="Importance", y="Feature", data=importance_df.sort_values("Importance", ascending=False), ax=ax)
st.pyplot(fig)

# ------------------------------------------------------------
# 5️⃣ Correlation Matrix Visualization
# ------------------------------------------------------------
st.header("🔗 Feature Correlation Matrix")
fig2, ax2 = plt.subplots(figsize=(10, 8))
sns.heatmap(corr, annot=False, cmap="Greens", ax=ax2)
st.pyplot(fig2)

# ------------------------------------------------------------
# 6️⃣ Optional: Best Model Info
# ------------------------------------------------------------
try:
    model = joblib.load("./data/processed/best_model.pkl")
    st.header("🧠 Best Model Summary")
    st.write(model)
except Exception:
    st.warning("⚠️ Could not load best_model.pkl")
