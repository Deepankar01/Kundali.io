def generate_bhava_summary(chart):
    bhava_data = {}

    # Map of sign lords
    sign_lords = {
        "Aries": "Mars", "Taurus": "Venus", "Gemini": "Mercury", "Cancer": "Moon",
        "Leo": "Sun", "Virgo": "Mercury", "Libra": "Venus", "Scorpio": "Mars",
        "Sagittarius": "Jupiter", "Capricorn": "Saturn", "Aquarius": "Saturn", "Pisces": "Jupiter"
    }

    # Reverse map: sign to house number
    sign_to_house = {v: int(k) for k, v in chart["houses"].items()}

    # Grahas in each house (by sign placement)
    house_grahas = {i: [] for i in range(1, 13)}
    for graha, data in chart["grahas"].items():
        sign = data["sign"]
        house_num = sign_to_house.get(sign)
        if house_num:
            house_grahas[house_num].append(graha)

    # Bhava structure
    for i in range(1, 13):
        sign = chart["houses"][str(i)]
        lord = sign_lords[sign]
        lord_placement = chart["grahas"][lord]["sign"]
        lord_house = sign_to_house[lord_placement]
        bhava_data[i] = {
            "Sign": sign,
            "HouseLord": lord,
            "LordPlacedInSign": lord_placement,
            "LordPlacedInHouse": lord_house,
            "PlanetsInHouse": house_grahas[i]
        }

    return bhava_data
