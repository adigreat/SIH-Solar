PERFORMANCE_RATIO = 0.80
DEGRADATION_RATE = 0.005
PROJECT_LIFETIME = 25


DAYS_IN_MONTH = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


def calculate_monthly_generation(
    solar_irradiance,
    capacity_mw,
    month,
    performance_ratio=PERFORMANCE_RATIO
):
    """
    Calculate monthly electricity generation.

    solar_irradiance:
        Average daily solar energy
        in kWh/m²/day

    capacity_mw:
        Solar plant capacity in MW

    month:
        Month number from 1 to 12

    performance_ratio:
        Accounts for system losses.
    """

    days = DAYS_IN_MONTH[month]

    generation_mwh = (
        solar_irradiance
        * capacity_mw
        * days
        * performance_ratio
    )

    return generation_mwh


def calculate_annual_generation(
    monthly_data,
    capacity_mw,
    performance_ratio=PERFORMANCE_RATIO
):
    """
    Calculate total annual electricity generation
    from monthly solar data.
    """

    total_generation = 0

    for _, row in monthly_data.iterrows():

        month = int(row["month"])

        solar_irradiance = float(
            row["solar_irradiance"]
        )

        monthly_generation = calculate_monthly_generation(
            solar_irradiance,
            capacity_mw,
            month,
            performance_ratio
        )

        total_generation += monthly_generation

    return total_generation


def calculate_degraded_generation(
    first_year_generation,
    year,
    degradation_rate=DEGRADATION_RATE
):
    """
    Calculate generation for a particular year
    after panel degradation.
    """

    return (
        first_year_generation
        * (1 - degradation_rate) ** (year - 1)
    )


def calculate_lifetime_generation(
    first_year_generation,
    lifetime=PROJECT_LIFETIME,
    degradation_rate=DEGRADATION_RATE
):
    """
    Calculate generation over the entire
    project lifetime.
    """

    results = []

    for year in range(1, lifetime + 1):

        generation = calculate_degraded_generation(
            first_year_generation,
            year,
            degradation_rate
        )

        results.append({
            "year": year,
            "generation_mwh": generation
        })

    return results