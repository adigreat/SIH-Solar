from fastapi import FastAPI, HTTPException
import pandas as pd
from services.budget_optimizer import optimize_budget

# ==========================================
# CREATE FASTAPI APPLICATION
# ==========================================

app = FastAPI(
    title="SuryaNivesh API",
    description="Rural Solar Investment Intelligence API",
    version="1.0.0"
)


# ==========================================
# LOAD DATA
# ==========================================

VILLAGES_FILE = "../data/villages.csv"

RANKING_FILE = (
    "../data/processed/"
    "village_investment_ranking.csv"
)

MONTHLY_SOLAR_FILE = (
    "../data/processed/"
    "village_monthly_solar_dataset.csv"
)


villages = pd.read_csv(
    VILLAGES_FILE
)

ranking = pd.read_csv(
    RANKING_FILE
)

solar_data = pd.read_csv(
    MONTHLY_SOLAR_FILE
)


# ==========================================
# BASIC ROOT ENDPOINT
# ==========================================

@app.get("/")
def home():

    return {
        "message": "Welcome to SuryaNivesh API",
        "status": "running"
    }


# ==========================================
# GET ALL VILLAGES
# ==========================================

@app.get("/villages")
def get_villages():

    data = ranking.to_dict(
        orient="records"
    )

    return {
        "count": len(data),
        "villages": data
    }


# ==========================================
# GET ONE VILLAGE
# ==========================================

@app.get("/villages/{village_id}")
def get_village(
    village_id: str
):

    village = ranking[
        ranking["village_id"] == village_id
    ]

    if village.empty:

        raise HTTPException(
            status_code=404,
            detail="Village not found"
        )

    result = village.iloc[0].to_dict()

    return result


# ==========================================
# GET VILLAGE SOLAR DATA
# ==========================================

@app.get("/villages/{village_id}/solar")
def get_village_solar(
    village_id: str
):

    village_solar = solar_data[
        solar_data["village_id"] == village_id
    ]

    if village_solar.empty:

        raise HTTPException(
            status_code=404,
            detail="Solar data not found"
        )

    return {
        "village_id": village_id,
        "data": village_solar.to_dict(
            orient="records"
        )
    }


# ==========================================
# GET RANKING
# ==========================================

@app.get("/ranking")
def get_ranking():

    sorted_ranking = ranking.sort_values(
        "investment_score",
        ascending=False
    )

    return {
        "count": len(sorted_ranking),
        "ranking": sorted_ranking.to_dict(
            orient="records"
        )
    }


# ==========================================
# HEALTH CHECK
# ==========================================

@app.get("/health")
def health_check():

    return {
        "status": "healthy",
        "villages_loaded": len(villages),
        "ranking_loaded": len(ranking),
        "solar_records_loaded": len(solar_data)
    }
# ==========================================
# BUDGET OPTIMIZATION
# ==========================================

@app.get("/investment-plan")
def get_investment_plan(
    budget: float
):

    if budget <= 0:

        raise HTTPException(
            status_code=400,
            detail="Budget must be greater than zero"
        )

    # Run budget optimizer
    selected, total_cost = optimize_budget(
        ranking,
        budget,
        capacity_per_village_mw=1
    )

    # Convert selected villages to DataFrame
    selected_df = pd.DataFrame(
        selected
    )

    # No villages can be selected
    if selected_df.empty:

        return {
            "budget": budget,
            "selected_villages": [],
            "total_investment": 0,
            "remaining_budget": budget,
            "expected_annual_generation_mwh": 0
        }

    # Calculate expected generation
    total_generation = (
        selected_df[
            "annual_generation_mwh"
        ].sum()
    )

    # Convert DataFrame to JSON-safe records
    selected_villages = (
        selected_df
        .where(pd.notnull(selected_df), None)
        .to_dict(orient="records")
    )

    return {

        "budget": budget,

        "selected_villages":
            selected_villages,

        "total_investment":
            float(total_cost),

        "remaining_budget":
            float(
                budget - total_cost
            ),

        "expected_annual_generation_mwh":
            float(total_generation),

        "expected_annual_generation_gwh":
            float(
                total_generation / 1000
            )
    }