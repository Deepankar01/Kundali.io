def detect_yogas(chart):
    yogas = []

    signs_order = [
        "Aries",
        "Taurus",
        "Gemini",
        "Cancer",
        "Leo",
        "Virgo",
        "Libra",
        "Scorpio",
        "Sagittarius",
        "Capricorn",
        "Aquarius",
        "Pisces",
    ]

    # Sign occupancy
    sign_occupancy = {sign: [] for sign in signs_order}
    for graha, data in chart["grahas"].items():
        sign_occupancy[data["sign"]].append(graha)

    movable = {"Aries", "Cancer", "Libra", "Capricorn"}
    fixed = {"Taurus", "Leo", "Scorpio", "Aquarius"}
    dual = {"Gemini", "Virgo", "Sagittarius", "Pisces"}

    benefics = {"Mercury", "Venus", "Jupiter"}
    malefics = {"Sun", "Mars", "Saturn"}
    non_luminaries = [g for g in chart["grahas"] if g not in ("Sun", "Moon")]

    # Asraya Yogas
    if all(chart["grahas"][g]["sign"] in movable for g in non_luminaries):
        yogas.append("Rajju Yoga")
    if all(chart["grahas"][g]["sign"] in fixed for g in non_luminaries):
        yogas.append("Musala Yoga")
    if all(chart["grahas"][g]["sign"] in dual for g in non_luminaries):
        yogas.append("Nala Yoga")

    # Dala Yogas
    if all(g in benefics for g in non_luminaries if g in chart["grahas"]):
        yogas.append("Maala Yoga")
    if all(g in malefics for g in non_luminaries if g in chart["grahas"]):
        yogas.append("Sarpa Yoga")

    # Sankhya Yogas
    occupied_signs = set([data["sign"] for data in chart["grahas"].values()])
    count = len(occupied_signs)
    if count == 1:
        yogas.append("Gola Yoga")
    elif count == 2:
        yogas.append("Yuga Yoga")
    elif count == 3:
        yogas.append("Soola Yoga")
    elif count == 4:
        yogas.append("Kedara Yoga")
    elif count == 5:
        yogas.append("Paasa Yoga")
    elif count == 6:
        yogas.append("Daama Yoga")
    elif count == 7:
        yogas.append("Veena Yoga")

    # Akriti Yogas
    lagna = chart["ascendant"]
    lagna_index = signs_order.index(lagna)
    sign_4 = signs_order[(lagna_index + 3) % 12]
    sign_7 = signs_order[(lagna_index + 6) % 12]
    sign_10 = signs_order[(lagna_index + 9) % 12]

    # Kendras from Lagna
    kendras_from_lagna = {lagna, sign_4, sign_7, sign_10}

    gada_zones = [("Aries", "Cancer"), ("Libra", "Capricorn")]
    for zone1, zone2 in gada_zones:
        if sign_occupancy[zone1] and sign_occupancy[zone2]:
            yogas.append("Gada Yoga")
            break

    if (
        any(p in benefics for p in sign_occupancy[lagna])
        and any(p in benefics for p in sign_occupancy[sign_7])
        and any(p in malefics for p in sign_occupancy[sign_4])
        and any(p in malefics for p in sign_occupancy[sign_10])
    ):
        yogas.append("Vajra Yoga")

    if (
        sign_occupancy[lagna]
        and sign_occupancy[sign_7]
        and sign_occupancy[sign_4]
        and sign_occupancy[sign_10]
    ):
        yogas.append("Yava Yoga")

    # Sakata Yoga
    jup_sign = chart["grahas"]["Jupiter"]["sign"]
    moon_sign = chart["grahas"]["Moon"]["sign"]
    jup_index = signs_order.index(jup_sign)
    moon_index = signs_order.index(moon_sign)
    if abs(jup_index - moon_index) % 12 == 6:
        yogas.append("Sakata Yoga")

    # Chakra Yoga
    if (
        sign_occupancy[lagna]
        and sign_occupancy[sign_4]
        and sign_occupancy[sign_7]
        and sign_occupancy[sign_10]
    ):
        yogas.append("Chakra Yoga")

    # Gajakesari Yoga
    kendras_from_moon = {signs_order[(moon_index + offset) % 12] for offset in [0, 3, 6, 9]}
    if chart["grahas"]["Jupiter"]["sign"] in kendras_from_moon:
        yogas.append("Gajakesari Yoga")

    # Chamara Yoga
    exalted = {"Mercury": "Virgo", "Jupiter": "Cancer"}
    own_signs = {"Mercury": {"Gemini", "Virgo"}, "Jupiter": {"Sagittarius", "Pisces"}}
    merc_sign = chart["grahas"]["Mercury"]["sign"]
    if jup_sign in kendras_from_lagna and (
        jup_sign in own_signs["Jupiter"] or jup_sign == exalted["Jupiter"]
    ):
        yogas.append("Chamara Yoga")
    if merc_sign in kendras_from_lagna and (
        merc_sign in own_signs["Mercury"] or merc_sign == exalted["Mercury"]
    ):
        yogas.append("Chamara Yoga")

    # Lunar Yogas
    surrounding = set()
    moon_pos = signs_order.index(moon_sign)
    for offset in [11, 1]:
        neighbor_sign = signs_order[(moon_pos + offset) % 12]
        surrounding.update(sign_occupancy[neighbor_sign])

    if surrounding:
        if "Sun" not in surrounding:
            yogas.append("Duradhara Yoga")
        if all(g in benefics for g in surrounding):
            yogas.append("Sunapha/Anapha Yoga")
    if not surrounding and not sign_occupancy[moon_sign]:
        yogas.append("Kemadruma Yoga")

    return list(set(yogas))
