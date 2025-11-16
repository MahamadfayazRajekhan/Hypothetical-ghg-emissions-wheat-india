import pandas as pd

df = pd.read_csv("wheat_farmers_4000.csv")

EF_direct = 0.01
EF_indirect = 0.004
N2O_conversion = 1.57
GWP_N2O = 298

df["N2O_N_direct"] = df["N_applied_kg_per_ha"] * EF_direct
df["N2O_N_indirect"] = df["N_applied_kg_per_ha"] * EF_indirect
df["Total_N2O_N"] = df["N2O_N_direct"] + df["N2O_N_indirect"]
df["N2O_gas_kg_per_ha"] = df["Total_N2O_N"] * N2O_conversion
df["CO2e_kg_per_ha"] = df["N2O_gas_kg_per_ha"] * GWP_N2O

df.to_csv("data/wheat_farmers_4000_with_emissions.csv", index=False)
print("Emission dataset saved.")
