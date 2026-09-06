import pandas as pd

from services.solar_engine import (
    calculate_annual_generation,
    calculate_lifetime_generation
)

from services.financial_engine import (
    calculate_capex,
    calculate_annual_cash_flow,
    calculate_electricity_value,
    calculate_annual_opex,
    calculate_payback_period,
    calculate_roi
)


# ==========================================
# LOAD SOLAR DATA
# ==========================================

solar_data = pd.read_csv(
    "../data/processed/"
    "village_monthly_solar_dataset.csv"
)


# ==========================================
# SELECT VILLAGE
# ==========================================

village = solar_data[
    solar_data["village_id"] == "V001"
]


# ==========================================
# PLANT SIZE
# ==========================================

capacity_mw = 1


# ==========================================
# SOLAR GENERATION
# ==========================================

first_year_generation = calculate_annual_generation(
    village,
    capacity_mw
)


lifetime_generation = calculate_lifetime_generation(
    first_year_generation
)


# ==========================================
# FINANCIAL MODEL
# ==========================================

capex = calculate_capex(
    capacity_mw
)


annual_opex = calculate_annual_opex(
    capex
)


cash_flows = []


for year_data in lifetime_generation:

    generation = year_data[
        "generation_mwh"
    ]

    electricity_value = calculate_electricity_value(
        generation
    )

    cash_flow = calculate_annual_cash_flow(
        generation,
        capex
    )

    cash_flows.append(
        cash_flow
    )


# ==========================================
# PAYBACK
# ==========================================

payback = calculate_payback_period(
    cash_flows,
    capex
)


# ==========================================
# TOTAL PROFIT
# ==========================================

total_cash_flow = sum(
    cash_flows
)


total_profit = (
    total_cash_flow
    - capex
)


roi = calculate_roi(
    total_profit,
    capex
)


# ==========================================
# DISPLAY RESULTS
# ==========================================

print("\n================================")
print("SURYA NIVESH FINANCIAL ANALYSIS")
print("================================")


print(
    f"\nVillage: "
    f"{village['village_name'].iloc[0]}"
)


print(
    f"Plant capacity: "
    f"{capacity_mw} MW"
)


print(
    f"\nInitial investment (CAPEX): "
    f"₹{capex:,.0f}"
)


print(
    f"Annual OPEX: "
    f"₹{annual_opex:,.0f}"
)


print(
    f"\nYear 1 generation: "
    f"{first_year_generation:,.2f} MWh"
)


print(
    f"\n25-year total cash flow: "
    f"₹{total_cash_flow:,.0f}"
)


if payback:

    print(
        f"Payback period: "
        f"{payback} years"
    )

else:

    print(
        "Payback period: "
        "Investment not recovered"
    )


print(
    f"25-year ROI: "
    f"{roi:.2f}%"
)