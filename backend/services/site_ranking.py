def normalize_higher_is_better(
    value,
    minimum,
    maximum
):
    """
    Convert a value to a 0-100 score.

    Higher value = better score.
    """

    if maximum == minimum:
        return 100

    return (
        (value - minimum)
        / (maximum - minimum)
    ) * 100


def normalize_lower_is_better(
    value,
    minimum,
    maximum
):
    """
    Convert a value to a 0-100 score.

    Lower value = better score.
    """

    if maximum == minimum:
        return 100

    return (
        (maximum - value)
        / (maximum - minimum)
    ) * 100


def calculate_site_score(
    solar_score,
    financial_score,
    grid_score,
    demand_score=50,
    infrastructure_score=50
):
    """
    Calculate overall village investment score.

    Weights:

    Solar potential       30%
    Financial return      25%
    Grid accessibility    20%
    Energy demand         15%
    Infrastructure        10%
    """

    score = (
        solar_score * 0.30
        + financial_score * 0.25
        + grid_score * 0.20
        + demand_score * 0.15
        + infrastructure_score * 0.10
    )

    return score