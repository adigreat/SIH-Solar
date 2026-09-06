import pandas as pd


def calculate_monthly_solar_data(
    daily_data
):
    """
    Convert daily solar data into
    monthly averages.
    """

    data = daily_data.copy()

    data["date"] = pd.to_datetime(
        data["date"],
        format="%Y%m%d"
    )

    data["month"] = data["date"].dt.month

    monthly = (
        data
        .groupby("month")
        .agg(
            solar_irradiance=(
                "solar_irradiance",
                "mean"
            ),
            temperature=(
                "temperature",
                "mean"
            )
        )
        .reset_index()
    )
    def prepare_solar_resource(
    monthly_data
):
     data = monthly_data.copy()

    data = data.rename(
        columns={
            "solar_irradiance": "solar_resource",
            "temperature": "avg_temperature"
        }
    )

    return data
    return monthly