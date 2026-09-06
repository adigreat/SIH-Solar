import pandas as pd

from services.solar_engine import (
    calculate_annual_generation,
    calculate_lifetime_generation
)

from services.financial_engine import (
    calculate_capex,
    calculate_annual_cash_flow,
    calculate_payback_period,
    calculate_roi
)
from services.site_ranking import (
    normalize_higher_is_better,
    normalize_lower_is_better,
    calculate_site_score
)


# ==========================================
# LOAD DATA
# ==========================================

solar_data = pd.read_csv(
    "../data/processed/"
    "village_monthly_solar_dataset.csv"
)

villages = pd.read_csv(
    "../data/villages.csv"
)


# ==========================================
# PLANT CONFIGURATION
# ==========================================

capacity_mw = 1


results = []


# ==========================================
# ANALYZE EVERY VILLAGE
# ==========================================

for village_id in villages["id"]:

    village_solar = solar_data[
        solar_data["village_id"] == village_id
    ]

    if village_solar.empty:
        continue

    village_name = (
        village_solar["village_name"]
        .iloc[0]
    )

    # --------------------------------------
    # SOLAR GENERATION
    # --------------------------------------

    annual_generation = (
        calculate_annual_generation(
            village_solar,
            capacity_mw
        )
    )


    # --------------------------------------
    # FINANCIAL MODEL
    # --------------------------------------

    capex = calculate_capex(
        capacity_mw
    )

    lifetime_generation = (
        calculate_lifetime_generation(
            annual_generation
        )
    )

    cash_flows = []

    for year_data in lifetime_generation:

        cash_flow = (
            calculate_annual_cash_flow(
                year_data["generation_mwh"],
                capex
            )
        )

        cash_flows.append(
            cash_flow
        )

    payback = calculate_payback_period(
        cash_flows,
        capex
    )

    total_cash_flow = sum(
        cash_flows
    )

    total_profit = (
        total_cash_flow - capex
    )

    roi = calculate_roi(
        total_profit,
        capex
    )


    # --------------------------------------
    # STORE RESULTS
    # --------------------------------------

    results.append({

        "village_id": village_id,

        "village_name": village_name,

        "grid_distance_km":
            villages[
                villages["id"] == village_id
            ]["grid_distance_km"].iloc[0],

        "annual_generation_mwh":
            annual_generation,

        "payback_years":
            payback
            if payback is not None
            else 999,

        "roi_percent":
            roi
    })


# ==========================================
# CREATE DATAFRAME
# ==========================================

results_df = pd.DataFrame(
    results
)


# ==========================================
# SOLAR SCORE
# ==========================================

results_df["solar_score"] = (
    results_df[
        "annual_generation_mwh"
    ].apply(
        lambda x:
        normalize_higher_is_better(
            x,
            results_df[
                "annual_generation_mwh"
            ].min(),
            results_df[
                "annual_generation_mwh"
            ].max()
        )
    )
)


# ==========================================
# FINANCIAL SCORE
# ==========================================

results_df["financial_score"] = (
    results_df[
        "roi_percent"
    ].apply(
        lambda x:
        normalize_higher_is_better(
            x,
            results_df[
                "roi_percent"
            ].min(),
            results_df[
                "roi_percent"
            ].max()
        )
    )
)


# ==========================================
# GRID SCORE
# ==========================================

results_df["grid_score"] = (
    results_df[
        "grid_distance_km"
    ].apply(
        lambda x:
        normalize_lower_is_better(
            x,
            results_df[
                "grid_distance_km"
            ].min(),
            results_df[
                "grid_distance_km"
            ].max()
        )
    )
)


# ==========================================
# DEMAND + INFRASTRUCTURE
# ==========================================

results_df["demand_score"] = 50

results_df["infrastructure_score"] = 50


# ==========================================
# FINAL SCORE
# ==========================================

results_df["investment_score"] = (
    results_df.apply(
        lambda row:
        calculate_site_score(
            row["solar_score"],
            row["financial_score"],
            row["grid_score"],
            row["demand_score"],
            row["infrastructure_score"]
        ),
        axis=1
    )
)


# ==========================================
# RANK VILLAGES
# ==========================================

results_df = results_df.sort_values(
    "investment_score",
    ascending=False
).reset_index(
    drop=True
)


results_df["rank"] = (
    results_df.index + 1
)


# ==========================================
# DISPLAY
# ==========================================

print("\n==========================================")
print("       SURYA NIVESH SITE RANKING")
print("==========================================\n")


display_columns = [
    "rank",
    "village_name",
    "annual_generation_mwh",
    "grid_distance_km",
    "roi_percent",
    "payback_years",
    "investment_score"
]


print(
    results_df[
        display_columns
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
# SAVE
# ==========================================

results_df.to_csv(
    "../data/processed/"
    "village_investment_ranking.csv",
    index=False
)


print(
    "\nRanking saved to:"
)

print(
    "../data/processed/"
    "village_investment_ranking.csv"
)