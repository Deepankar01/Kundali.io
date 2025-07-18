def calcluate_navamsa_chart(chart):
    """
    Calculates Navamsa (D9) positions of all planets from Rasi chart.
    Returns a dictionary with planet -> navamsa sign and division number (1 to 9)
    """

    signs_order = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
                   "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

    # Sign type mapping
    sign_types = {
        "Aries": "movable", "Cancer": "movable", "Libra": "movable", "Capricorn": "movable",
        "Taurus": "fixed", "Leo": "fixed", "Scorpio": "fixed", "Aquarius": "fixed",
        "Gemini": "dual", "Virgo": "dual", "Sagittarius": "dual", "Pisces": "dual"
    }

    navamsa_chart = {}

    for graha, data in chart['grahas'].items():
        rasi = data['sign']
        degree = data['degree']

        # Determine which Navamsa division (1 to 9)
        division = int(degree // (30 / 9)) + 1  # Each division is 3.333... degrees

        # Determine start sign for Navamsa based on Rasi type
        sign_index = signs_order.index(rasi)
        if sign_types[rasi] == "movable":
            start_index = sign_index
        elif sign_types[rasi] == "fixed":
            start_index = (sign_index + 8) % 12  # 9th from the sign
        else:  # dual
            start_index = (sign_index + 4) % 12  # 5th from the sign

        # Navamsa sign is counted from the start
        navamsa_sign = signs_order[(start_index + division - 1) % 12]

        navamsa_chart[graha] = {
            "navamsa_sign": navamsa_sign,
            "division": division
        }

    return navamsa_chart
