import pandas as pd

from services.budget_optimizer import (
    optimize_budget
)


# ==========================================
# LOAD RANKING
# ==========================================

ranking = pd.read_csv(
    "../data/processed/"
    "village_investment_ranking.csv"
)


# ==========================================
# GOVERNMENT BUDGET
# ==========================================

# ₹10 crore
budget = 100_000_000


# ==========================================
# OPTIMIZE
# ==========================================

selected, total_cost = optimize_budget(
    ranking,
    budget,
    capacity_per_village_mw=1
)


# ==========================================
# CREATE DATAFRAME
# ==========================================

selected_df = pd.DataFrame(
    selected
)


# ==========================================
# DISPLAY RESULTS
# ==========================================

print("\n==========================================")
print("       SURYA NIVESH BUDGET OPTIMIZER")
print("==========================================")

print(
    f"\nGovernment budget: "
    f"₹{budget:,.0f}"
)

print(
    f"Available budget: "
    f"₹{budget / 10_000_000:.2f} crore"
)

print(
    f"\nCost per village: "
    f"₹{40_000_000 / 10_000_000:.2f} crore"
)

print(
    f"\nVillages selected: "
    f"{len(selected_df)}"
)

print(
    f"Total investment: "
    f"₹{total_cost:,.0f}"
)

print(
    f"Remaining budget: "
    f"₹{budget - total_cost:,.0f}"
)


# ==========================================
# SELECTED VILLAGES
# ==========================================

print("\n==========================================")
print("          RECOMMENDED INVESTMENTS")
print("==========================================\n")


columns = [
    "rank",
    "village_name",
    "annual_generation_mwh",
    "grid_distance_km",
    "roi_percent",
    "payback_years",
    "investment_score"
]


print(
    selected_df[
        columns
    ].to_string(
        index=False,
        formatters={
            "annual_generation_mwh":
                "{:.2f}".format,

            "grid_distance_km":
                "{:.2f}".format,

            "roi_percent":
                "{:.2f}%".format,

            "investment_score":
                "{:.2f}".format
        }
    )
)


# ==========================================
# TOTAL GENERATION
# ==========================================

total_generation = (
    selected_df[
        "annual_generation_mwh"
    ].sum()
)


print("\n==========================================")
print("              IMPACT")
print("==========================================")

print(
    f"\nExpected annual generation: "
    f"{total_generation:,.2f} MWh"
)

print(
    f"Expected annual generation: "
    f"{total_generation / 1000:,.2f} GWh"
)