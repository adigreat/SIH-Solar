import pandas as pd

from services.solar_engine import (
    calculate_annual_generation,
    calculate_lifetime_generation
)


# Load MONTHLY solar dataset
solar_data = pd.read_csv(
    "../data/processed/"
    "village_monthly_solar_dataset.csv"
)


# Select Village A
village = solar_data[
    solar_data["village_id"] == "V001"
]


# Assume 1 MW plant
capacity_mw = 1


# Calculate annual generation
annual_generation = calculate_annual_generation(
    village,
    capacity_mw
)


print("\n==============================")
print("SOLAR GENERATION")
print("==============================")


print(
    f"Village: "
    f"{village['village_name'].iloc[0]}"
)


print(
    f"Plant capacity: "
    f"{capacity_mw} MW"
)


print(
    f"Expected annual generation: "
    f"{annual_generation:.2f} MWh"
)


print(
    f"Expected annual generation: "
    f"{annual_generation / 1000:.2f} GWh"
)


# 25-year projection
lifetime = calculate_lifetime_generation(
    annual_generation
)


lifetime_df = pd.DataFrame(
    lifetime
)


print("\n==============================")
print("25 YEAR PROJECTION")
print("==============================")


print(
    lifetime_df.to_string(
        index=False
    )
)


# Total lifetime generation
total_generation = (
    lifetime_df["generation_mwh"].sum()
)


print("\n==============================")
print("TOTAL")
print("==============================")


print(
    f"25-year generation: "
    f"{total_generation:.2f} MWh"
)


print(
    f"25-year generation: "
    f"{total_generation / 1000:.2f} GWh"
)