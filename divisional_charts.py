# not to be used
def calculate_divisional_chart(chart, division_factor, division_rules):
    """
    Generic function to calculate divisional charts (D9, D10, D7, etc.)
    Inputs:
    - chart: output of generate_rasi_chart()
    - division_factor: e.g. 9 for D9, 10 for D10, etc.
    - division_rules: dict of how to determine start sign index for each sign type (movable, fixed, dual, odd, even)
    Returns:
    - Dictionary of planet -> divisional sign
    """

    signs_order = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
                   "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

    sign_types = {
        "Aries": "movable", "Cancer": "movable", "Libra": "movable", "Capricorn": "movable",
        "Taurus": "fixed", "Leo": "fixed", "Scorpio": "fixed", "Aquarius": "fixed",
        "Gemini": "dual", "Virgo": "dual", "Sagittarius": "dual", "Pisces": "dual"
    }

    divisional_chart = {}

    for graha, data in chart['grahas'].items():
        rasi = data['sign']
        degree = data['degree']
        rasi_index = signs_order.index(rasi)

        division = int(degree // (30 / division_factor)) + 1  # 1-based division

        # Determine start index
        if division_rules.get("type_based"):
            rasi_type = sign_types[rasi]
            start_offset = division_rules["type_based"][rasi_type]
        elif division_rules.get("odd_even_based"):
            is_odd = rasi_index % 2 == 0  # 0-based: Aries is 0 (odd-numbered sign)
            start_offset = division_rules["odd_even_based"]["odd" if is_odd else "even"]
        else:
            start_offset = 0

        start_index = (rasi_index + start_offset) % 12
        div_sign = signs_order[(start_index + division - 1) % 12]

        divisional_chart[graha] = {
            "division": division,
            "sign": div_sign
        }

    return divisional_chart

# D10 (Dasamsa) rules per BPHS: movable -> self, fixed -> 9th, dual -> 5th
d10_rules = {
    "type_based": {
        "movable": 0,
        "fixed": 8,
        "dual": 4
    }
}

# D7 (Saptamsa) rules: odd signs -> from self, even signs -> from 7th
d7_rules = {
    "odd_even_based": {
        "odd": 0,
        "even": 6
    }
}
