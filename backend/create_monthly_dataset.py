import pandas as pd
import os


INPUT_FILE = "../data/processed/village_solar_dataset.csv"

OUTPUT_FILE = (
    "../data/processed/"
    "village_monthly_solar_dataset.csv"
)


def create_monthly_dataset():

    print("Loading solar dataset...")

    data = pd.read_csv(INPUT_FILE)

    print(f"Daily records: {len(data)}")

    # Convert date
    data["date"] = pd.to_datetime(
        data["date"]
    )

    # Make sure solar values are numeric
    data["solar_irradiance"] = pd.to_numeric(
        data["solar_irradiance"],
        errors="coerce"
    )

    # Remove missing values
    data = data.dropna(
        subset=["solar_irradiance"]
    )

    # Remove invalid negative values
    data = data[
        data["solar_irradiance"] >= 0
    ]

    # Create month number
    data["month"] = data["date"].dt.month

    # Calculate monthly averages
    monthly = (
        data
        .groupby(
            [
                "village_id",
                "village_name",
                "month"
            ]
        )
        .agg(
            solar_irradiance=(
                "solar_irradiance",
                "mean"
            ),
            avg_temperature=(
                "avg_temperature",
                "mean"
            ),
            days_observed=(
                "date",
                "count"
            )
        )
        .reset_index()
    )

    # Sort
    monthly = monthly.sort_values(
        [
            "village_id",
            "month"
        ]
    )

    # Create folder
    os.makedirs(
        "../data/processed",
        exist_ok=True
    )

    # Save
    monthly.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print("\n================================")
    print("MONTHLY DATASET CREATED")
    print("================================")

    print(
        f"Saved to: {OUTPUT_FILE}"
    )

    print(
        f"Total records: {len(monthly)}"
    )

    print("\nFirst rows:")

    print(
        monthly.head(12)
    )


if __name__ == "__main__":
    create_monthly_dataset()