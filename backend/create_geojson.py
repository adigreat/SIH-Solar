import pandas as pd
import json


# ==========================================
# LOAD DATA
# ==========================================

villages = pd.read_csv(
    "../data/villages.csv"
)

ranking = pd.read_csv(
    "../data/processed/"
    "village_investment_ranking.csv"
)


# ==========================================
# MERGE VILLAGE + RANKING DATA
# ==========================================

data = villages.merge(
    ranking,
    left_on="id",
    right_on="village_id",
    how="left",
    suffixes=("", "_ranking")
)
# ==========================================
# CREATE GEOJSON FEATURES
# ==========================================

features = []


for _, row in data.iterrows():

    feature = {
        "type": "Feature",

        "geometry": {
            "type": "Point",

            "coordinates": [
                float(row["longitude"]),
                float(row["latitude"])
            ]
        },

        "properties": {

            "id":
                row["id"],

            "name":
                row["name"],

            "district":
                row["district"],

            "population":
                row["population"],

            "grid_distance_km":
                row["grid_distance_km"],

            "investment_score":
                row["investment_score"],

            "annual_generation_mwh":
                row["annual_generation_mwh"],

            "roi_percent":
                row["roi_percent"],

            "payback_years":
                row["payback_years"],

            "rank":
                row["rank"]
        }
    }

    features.append(feature)


# ==========================================
# CREATE GEOJSON
# ==========================================

geojson = {

    "type": "FeatureCollection",

    "features": features
}


# ==========================================
# SAVE
# ==========================================

output_file = (
    "../data/processed/"
    "villages.geojson"
)


with open(
    output_file,
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        geojson,
        file,
        indent=2
    )


print("\n================================")
print("GEOJSON CREATED")
print("================================")

print(
    f"\nSaved to:\n{output_file}"
)

print(
    f"\nTotal villages: "
    f"{len(features)}"
)