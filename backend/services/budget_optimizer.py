CAPEX_PER_MW = 40_000_000


def optimize_budget(
    villages,
    budget,
    capacity_per_village_mw=1
):
    """
    Select the highest-ranked villages
    that fit within the available budget.

    Parameters
    ----------
    villages : pandas DataFrame
        Ranked village dataset.

    budget : float
        Available government budget in rupees.

    capacity_per_village_mw : float
        Solar capacity installed at each
        selected village.
    """

    cost_per_village = (
        CAPEX_PER_MW
        * capacity_per_village_mw
    )

    selected = []

    total_cost = 0

    for _, village in villages.iterrows():

        if (
            total_cost + cost_per_village
            <= budget
        ):

            selected.append(
                village
            )

            total_cost += cost_per_village

    return selected, total_cost