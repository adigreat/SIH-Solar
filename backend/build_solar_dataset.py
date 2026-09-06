import os
import pandas as pd

from services.nasa_power import fetch_solar_data
from services.solar_processing import calculate_monthly_solar_data


# Load village dataset
villages = pd.read_csv("../data/villages.csv")


# Create output folder
os.makedirs("../data/raw", exist_ok=True)


# Process every village
for _, village in villages.iterrows():

    latitude = village["latitude"]
    longitude = village["longitude"]

    print(
        f"Fetching solar data for {village['name']} "
        f"({latitude}, {longitude})..."
    )

    # Fetch NASA POWER data
    solar_data = fetch_solar_data(
        latitude,
        longitude
    )

    # Convert daily data → monthly data
    monthly_data = calculate_monthly_solar_data(
        solar_data
    )

    # Add village information
    monthly_data["village_id"] = village["id"]
    monthly_data["village_name"] = village["name"]

    # Save result
    output_file = f"../data/raw/{village['id']}_solar.csv"

    monthly_data.to_csv(
        output_file,
        index=False
    )

    print(f"Saved: {output_file}")


print("\nAll villages processed successfully!")