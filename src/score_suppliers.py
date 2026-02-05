import pandas as pd
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv("data/processed/supplier_kpis.csv")

scaler = MinMaxScaler()
scaled = scaler.fit_transform(df[["avg_cost", "avg_delivery_days", "avg_quality_issues"]])

df[["cost_score", "delivery_score", "quality_score"]] = scaled

# Higher compliance = better
df["compliance_score"] = df["compliance_rate"]

# Composite score (weights adjustable)
df["final_score"] = (
    0.4 * (1 - df["cost_score"]) +
    0.3 * (1 - df["delivery_score"]) +
    0.2 * (1 - df["quality_score"]) +
    0.1 * df["compliance_score"]
)

df = df.sort_values("final_score", ascending=False)
df.to_csv("data/processed/supplier_scores.csv", index=False)

print("🏆 Supplier performance scores generated")
print(df[["supplier", "final_score"]])
