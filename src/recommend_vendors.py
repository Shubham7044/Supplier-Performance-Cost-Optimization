import pandas as pd

df = pd.read_csv("data/processed/supplier_scores.csv")

best_vendor = df.iloc[0]
worst_vendor = df.iloc[-1]

print(f"✅ Best Supplier: {best_vendor['supplier']} (Score: {round(best_vendor['final_score'],3)})")
print(f"⚠️ High-Risk Supplier: {worst_vendor['supplier']} (Score: {round(worst_vendor['final_score'],3)})")

print("\n💡 Recommendation:")
print(f"Consider shifting more volume to {best_vendor['supplier']} and reviewing contract terms with {worst_vendor['supplier']}.")
