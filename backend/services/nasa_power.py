import requests
import pandas as pd


NASA_POWER_URL = (
    "https://power.larc.nasa.gov/api/temporal/daily/point"
)


def fetch_solar_data(
    latitude,
    longitude,
    start_date="20250101",
    end_date="20251231"
):
    """
    Fetch daily solar and temperature data
    from NASA POWER for a specific location.
    """

    parameters = "ALLSKY_SFC_SW_DWN,T2M"

    params = {
        "parameters": parameters,
        "community": "RE",
        "longitude": longitude,
        "latitude": latitude,
        "start": start_date,
        "end": end_date,
        "format": "JSON"
    }

    response = requests.get(
        NASA_POWER_URL,
        params=params,
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    properties = data["properties"]
    parameter_data = properties["parameter"]

    solar = parameter_data["ALLSKY_SFC_SW_DWN"]
    temperature = parameter_data["T2M"]

    records = []

    for date in solar:

        records.append({
            "date": date,
            "solar_irradiance": solar[date],
            "temperature": temperature.get(date)
        })

    return pd.DataFrame(records)