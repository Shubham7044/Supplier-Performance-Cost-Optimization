import pandas as pd
import numpy as np
import random

suppliers = ["Supplier_A", "Supplier_B", "Supplier_C", "Supplier_D"]

rows = []
for i in range(1000):
    supplier = random.choice(suppliers)
    cost = round(random.uniform(100, 1000), 2)
    delivery_days = random.randint(1, 10)
    quality_issues = random.randint(0, 3)
    compliance = random.choice([0, 1])  # 1 = compliant, 0 = breach

    rows.append([supplier, cost, delivery_days, quality_issues, compliance])

df = pd.DataFrame(rows, columns=["supplier", "cost", "delivery_days", "quality_issues", "contract_compliance"])
df.to_csv("data/raw/supplier_transactions.csv", index=False)
print("✅ Supplier transaction data generated")
