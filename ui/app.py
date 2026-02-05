import streamlit as st
import pandas as pd

df = pd.read_csv("data/processed/supplier_scores.csv")

st.title("Supplier Performance & Cost Optimization Dashboard")

st.dataframe(df)

best = df.iloc[0]
worst = df.iloc[-1]

st.metric("Best Supplier", best["supplier"], round(best["final_score"], 3))
st.metric("High-Risk Supplier", worst["supplier"], round(worst["final_score"], 3))
