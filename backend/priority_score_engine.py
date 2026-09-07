import pandas as pd
import numpy as np
import joblib

scaler = joblib.load("package/scaler.pkl")
lr = joblib.load("package/lr_model.pkl")
rf = joblib.load("package/rf_model.pkl")
meta_model = joblib.load("package/meta_model.pkl")

FEATURE_COLUMNS = [
    "area_sq_km",
    "avg_solar_irradiance_kwh_m2_day",
    "annual_sun_hours",
    "seasonal_solar_variation_percent",
    "avg_temperature_c",
    "rainfall_mm_year",
    "cloud_cover_percent",
    "population",
    "households",
    "estimated_annual_electricity_demand_kwh",
    "agricultural_demand_kwh",
    "public_facility_demand_kwh",
    "grid_connected",
    "grid_reliability_percent",
    "avg_daily_power_hours",
    "outage_hours_month",
    "distance_to_grid_km",
    "existing_solar_capacity_kw",
    "existing_solar_project",
    "solar_pumps_count",
    "existing_solar_generation_kwh_year",
    "recommended_capacity_kw",
    "installation_cost_inr",
    "maintenance_cost_inr_year",
    "panel_efficiency_percent",
    "system_efficiency_percent",
    "expected_annual_generation_kwh",
    "electricity_value_inr_kwh",
    "degradation_rate_percent",
    "project_lifetime_years"
]

def calculate_priority_score(village_data):
    X = pd.DataFrame([village_data], columns=FEATURE_COLUMNS)

    X_scaled = scaler.transform(X)

    lr_pred = lr.predict(X_scaled)
    rf_pred = rf.predict(X_scaled)

    meta_input = np.column_stack([lr_pred, rf_pred])

    score = meta_model.predict(meta_input)[0]
    return float(np.clip(score, 0, 100))