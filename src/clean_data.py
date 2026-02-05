import pandas as pd
from pathlib import Path

RAW = Path("data/raw/supplier_transactions.csv")
OUT = Path("data/processed/supplier_kpis.csv")

df = pd.read_csv(RAW)

df = df.dropna()
df.to_csv(OUT, index=False)

print("✅ Cleaned supplier data saved")
