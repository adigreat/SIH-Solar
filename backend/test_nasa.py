from services.nasa_power import fetch_solar_data
from services.solar_processing import (
    calculate_monthly_solar_data
)


latitude = 20.005
longitude = 73.780


# ==========================================
# FETCH DAILY DATA
# ==========================================

daily_data = fetch_solar_data(
    latitude=latitude,
    longitude=longitude,
    start_date="20250101",
    end_date="20251231"
)


# ==========================================
# CONVERT TO MONTHLY
# ==========================================

monthly_data = calculate_monthly_solar_data(
    daily_data
)


print("\n================================")
print("NASA POWER MONTHLY SOLAR DATA")
print("================================")

print()

print(
    monthly_data.to_string(
        index=False
    )
)