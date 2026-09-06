    # ==========================================
# SURYANIVESH FINANCIAL MODEL
# ==========================================


# Cost of installing 1 MW solar capacity
CAPEX_PER_MW =40_000_000


# Annual operation & maintenance cost
# expressed as a percentage of initial CAPEX
OPEX_PERCENT = 0.02


# Value of electricity generated
# ₹ per kWh
ELECTRICITY_TARIFF = 5.0


# Project lifetime
PROJECT_LIFETIME = 25


# Annual degradation of solar panels
DEGRADATION_RATE = 0.005


def calculate_capex(
    capacity_mw,
    capex_per_mw=CAPEX_PER_MW
):
    """
    Calculate initial investment.
    """

    return capacity_mw * capex_per_mw


def calculate_annual_opex(
    capex,
    opex_percent=OPEX_PERCENT
):
    """
    Calculate annual operating cost.
    """

    return capex * opex_percent


def calculate_electricity_value(
    generation_mwh,
    electricity_tariff=ELECTRICITY_TARIFF
):
    """
    Convert generated electricity into
    monetary value.

    MWh → kWh
    """

    generation_kwh = generation_mwh * 1000

    value = (
        generation_kwh
        * electricity_tariff
    )

    return value


def calculate_annual_cash_flow(
    generation_mwh,
    capex,
    electricity_tariff=ELECTRICITY_TARIFF,
    opex_percent=OPEX_PERCENT
):
    """
    Calculate annual net cash flow.
    """

    electricity_value = calculate_electricity_value(
        generation_mwh,
        electricity_tariff
    )

    annual_opex = calculate_annual_opex(
        capex,
        opex_percent
    )

    net_cash_flow = (
        electricity_value
        - annual_opex
    )

    return net_cash_flow


def calculate_payback_period(
    annual_cash_flows,
    initial_investment
):
    """
    Determine how many years it takes
    to recover the initial investment.
    """

    cumulative_cash_flow = 0

    for year, cash_flow in enumerate(
        annual_cash_flows,
        start=1
    ):

        cumulative_cash_flow += cash_flow

        if cumulative_cash_flow >= initial_investment:

            return year

    # Investment never recovered
    return None


def calculate_roi(
    total_profit,
    initial_investment
):
    """
    Calculate return on investment.
    """

    if initial_investment == 0:
        return 0

    roi = (
        total_profit
        / initial_investment
    ) * 100

    return roi