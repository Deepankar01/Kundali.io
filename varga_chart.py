def calculate_varga_chart(chart, division_factor, division_rules):
    """
    Generic divisional chart calculator.
    Supports type-based and odd/even-based logic per BPHS.
    Input:
        chart: Output from generate_rasi_chart()
        division_factor: int, e.g., 9 for D9, 10 for D10
        division_rules: dict with one of:
            - "type_based": {"movable": x, "fixed": y, "dual": z}
            - "odd_even_based": {"odd": x, "even": y}
    Output:
        Dictionary: graha -> {division: int, sign: str}
    """

    signs_order = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
                   "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

    sign_types = {
        "Aries": "movable", "Cancer": "movable", "Libra": "movable", "Capricorn": "movable",
        "Taurus": "fixed", "Leo": "fixed", "Scorpio": "fixed", "Aquarius": "fixed",
        "Gemini": "dual", "Virgo": "dual", "Sagittarius": "dual", "Pisces": "dual"
    }

    varga_chart = {}

    for graha, data in chart['grahas'].items():
        rasi = data['sign']
        degree = data['degree']
        rasi_index = signs_order.index(rasi)

        # Determine which division segment (1 to division_factor)
        division = int(degree // (30 / division_factor)) + 1

        # Determine start offset based on rule
        if "type_based" in division_rules:
            rasi_type = sign_types[rasi]
            start_offset = division_rules["type_based"][rasi_type]
        elif "odd_even_based" in division_rules:
            is_odd = rasi_index % 2 == 0
            key = "odd" if is_odd else "even"
            start_offset = division_rules["odd_even_based"][key]
        else:
            start_offset = 0  # default

        start_index = (rasi_index + start_offset) % 12
        varga_sign = signs_order[(start_index + division - 1) % 12]

        varga_chart[graha] = {
            "division": division,
            "sign": varga_sign
        }

    return varga_chart
