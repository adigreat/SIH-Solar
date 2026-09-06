import pandas as pd
import folium


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
# MERGE DATA
# ==========================================

data = villages.merge(
    ranking,
    left_on="id",
    right_on="village_id",
    how="left",
    suffixes=("", "_ranking")
)


# ==========================================
# MAP CENTER
# ==========================================

map_center = [
    data["latitude"].mean(),
    data["longitude"].mean()
]


m = folium.Map(
    location=map_center,
    zoom_start=10
)


# ==========================================
# ADD VILLAGES
# ==========================================

for _, row in data.iterrows():

    score = row["investment_score"]


    # --------------------------------------
    # DETERMINE PRIORITY
    # --------------------------------------

    if score >= 75:

        color = "green"
        priority = "HIGH"

    elif score >= 50:

        color = "orange"
        priority = "MEDIUM"

    else:

        color = "red"
        priority = "LOW"


    # --------------------------------------
    # POPUP
    # --------------------------------------

    popup_text = f"""
    <div style="width: 250px">

        <h4>{row['name']}</h4>

        <b>Investment Priority:</b>
        {priority}<br><br>

        <b>Investment Score:</b>
        {score:.2f}/100<br>

        <b>Annual Generation:</b>
        {row['annual_generation_mwh']:.2f} MWh<br>

        <b>Grid Distance:</b>
        {row['grid_distance_km']:.2f} km<br>

        <b>ROI:</b>
        {row['roi_percent']:.2f}%<br>

        <b>Payback:</b>
        {row['payback_years']} years<br>

        <b>Rank:</b>
        #{int(row['rank'])}

    </div>
    """


    # --------------------------------------
    # ADD MARKER
    # --------------------------------------

    folium.Marker(

        location=[
            row["latitude"],
            row["longitude"]
        ],

        popup=folium.Popup(
            popup_text,
            max_width=300
        ),

        tooltip=(
            f"{row['name']} "
            f"| Score: {score:.1f}"
        ),

        icon=folium.Icon(
            color=color,
            icon="sun",
            prefix="fa"
        )

    ).add_to(m)


# ==========================================
# ADD LEGEND
# ==========================================

legend_html = """
<div style="
position: fixed;
bottom: 40px;
left: 40px;
width: 180px;
background-color: white;
border: 2px solid grey;
z-index: 9999;
padding: 10px;
font-size: 14px;
">

<b>Investment Priority</b><br><br>

<span style="color:green;">●</span>
High (≥75)<br>

<span style="color:orange;">●</span>
Medium (50–74)<br>

<span style="color:red;">●</span>
Low (<50)

</div>
"""


m.get_root().html.add_child(
    folium.Element(
        legend_html
    )
)


# ==========================================
# SAVE MAP
# ==========================================

output_file = (
    "../data/processed/"
    "village_map.html"
)


m.save(output_file)


print("\n================================")
print("MAP CREATED SUCCESSFULLY")
print("================================")

print(
    f"\nVillages displayed: "
    f"{len(data)}"
)

print(
    f"\nMap saved to:\n{output_file}"
)