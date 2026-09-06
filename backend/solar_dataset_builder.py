import os
import pandas as pd


RAW_FOLDER = "../data/raw"
PROCESSED_FOLDER = "../data/processed"

OUTPUT_FILE = "../data/processed/village_solar_dataset.csv"


def clean_solar_data(data):

    data = data.copy()

    # Show columns so we know exactly what we received
    print("Columns found:", data.columns.tolist())

    # NASA data may use different column names.
    # Standardize them here.

    if "solar_irradiance" not in data.columns:

        if "ALLSKY_SFC_SW_DWN" in data.columns:
            data = data.rename(
                columns={
                    "ALLSKY_SFC_SW_DWN": "solar_irradiance"
                }
            )

        elif "solar_resource" in data.columns:
            data = data.rename(
                columns={
                    "solar_resource": "solar_irradiance"
                }
            )

        else:
            raise ValueError(
                "Could not find a solar radiation column. "
                f"Available columns: {data.columns.tolist()}"
            )

    # Make sure month is numeric
    data["month"] = pd.to_numeric(
        data["month"],
        errors="coerce"
    )

    # Remove invalid month values
    data = data[
        (data["month"] >= 1) &
        (data["month"] <= 12)
    ]

    # Replace NASA missing-value markers
    data = data.replace(
        [-999, -999.0],
        pd.NA
    )

    # Convert solar data to numeric
    data["solar_irradiance"] = pd.to_numeric(
        data["solar_irradiance"],
        errors="coerce"
    )

    # Remove missing solar values
    data = data.dropna(
        subset=["solar_irradiance"]
    )

    # Solar radiation cannot be negative
    data = data[
        data["solar_irradiance"] >= 0
    ]

    return data


def build_dataset():

    os.makedirs(
        PROCESSED_FOLDER,
        exist_ok=True
    )

    all_data = []

    # Check raw folder
    if not os.path.exists(RAW_FOLDER):
        print("Raw data folder does not exist:")
        print(RAW_FOLDER)
        return

    # Read every village solar file
    for filename in os.listdir(RAW_FOLDER):

        if not filename.endswith("_solar.csv"):
            continue

        file_path = os.path.join(
            RAW_FOLDER,
            filename
        )

        print(f"\nReading {filename}...")

        data = pd.read_csv(file_path)

        # Clean data
        data = clean_solar_data(data)

        all_data.append(data)

        print(
            f"Cleaned rows: {len(data)}"
        )

    # Make sure files were found
    if not all_data:

        print(
            "\nNo solar files found in:"
        )
        print(RAW_FOLDER)

        return

    # Combine all villages
    final_dataset = pd.concat(
        all_data,
        ignore_index=True
    )

    # Sort by village and month
    final_dataset = final_dataset.sort_values(
        by=["village_id", "month"]
    )

    # Save final dataset
    final_dataset.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print("\n================================")
    print("DATASET CREATED SUCCESSFULLY")
    print("================================")

    print(
        f"\nSaved to:\n{OUTPUT_FILE}"
    )

    print(
        f"\nTotal rows: {len(final_dataset)}"
    )

    print(
        f"Total villages: "
        f"{final_dataset['village_id'].nunique()}"
    )

    print("\nColumns:")
    print(
        final_dataset.columns.tolist()
    )

    print("\nFirst 10 rows:")
    print(
        final_dataset.head(10)
    )


if __name__ == "__main__":
    build_dataset()