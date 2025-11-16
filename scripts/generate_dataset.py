import pandas as pd
import numpy as np

n = 4000
np.random.seed(42)

N_values = []
for _ in range(n):
    r = np.random.rand()
    if r < 0.20:
        N_values.append(np.random.choice([60, 70, 80]))
    elif r < 0.75:
        N_values.append(np.random.choice([100, 110, 120]))
    else:
        N_values.append(np.random.choice([140, 150, 160]))

df = pd.DataFrame({
    "farmer_id": range(1, n+1),
    "district": ["Gadag"] * n,
    "state": ["Karnataka"] * n,
    "crop": ["Wheat"] * n,
    "N_applied_kg_per_ha": N_values
})

df.to_csv("data/wheat_farmers_4000.csv", index=False)
print("Dataset saved.")

