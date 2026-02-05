import pandas as pd
from src.db import engine

df = pd.read_csv("data/processed/supplier_kpis.csv")
df.to_sql("supplier_transactions", engine, if_exists="replace", index=False)
print("✅ Data loaded into DB")
