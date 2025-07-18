# Re-define get_chara_karakas
def get_chara_karakas(chart):
    karaka_roles = [
        "Atmakaraka", "Amatyakaraka", "Bhratru Karaka", "Matru Karaka",
        "Pitru Karaka", "Putra Karaka", "Gnati Karaka", "Dara Karaka"
    ]

    signs_order = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
                   "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

    planet_longitudes = {}
    for graha, data in chart['grahas'].items():
        if graha not in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn", "Rahu"]:
            continue
        sign_index = signs_order.index(data["sign"])
        deg = data["degree"]
        adjusted_deg = 30 - deg if graha == "Rahu" else deg
        total_long = sign_index * 30 + adjusted_deg
        planet_longitudes[graha] = total_long

    sorted_planets = sorted(planet_longitudes.items(), key=lambda x: -x[1])
    karaka_result = {}
    for i, (graha, _) in enumerate(sorted_planets):
        if i < len(karaka_roles):
            karaka_result[karaka_roles[i]] = graha

    return karaka_result