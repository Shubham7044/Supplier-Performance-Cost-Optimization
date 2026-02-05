import pandas as pd
from src.db import engine

query = """
SELECT supplier,
       AVG(cost) AS avg_cost,
       AVG(delivery_days) AS avg_delivery_days,
       AVG(quality_issues) AS avg_quality_issues,
       AVG(contract_compliance) AS compliance_rate
FROM supplier_transactions
GROUP BY supplier;
"""

df = pd.read_sql(query, engine)
df.to_csv("data/processed/supplier_kpis.csv", index=False)
print("📊 Supplier KPIs computed")
