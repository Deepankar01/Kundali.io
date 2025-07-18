# 11th Bhava interpretation (Gains, Income, Fulfillment, Networks)
def interpret_11th_bhava(chart, shadbala):
    sign_in_11th = chart["houses"]["11"]
    bhava_lord_map = {
        "Aries": "Mars", "Taurus": "Venus", "Gemini": "Mercury", "Cancer": "Moon",
        "Leo": "Sun", "Virgo": "Mercury", "Libra": "Venus", "Scorpio": "Mars",
        "Sagittarius": "Jupiter", "Capricorn": "Saturn", "Aquarius": "Saturn", "Pisces": "Jupiter"
    }
    benefics = ["Jupiter", "Venus", "Mercury", "Moon"]
    malefics = ["Saturn", "Mars", "Sun", "Rahu", "Ketu"]

    bhava_lord = bhava_lord_map[sign_in_11th]
    lord_sign = chart["grahas"][bhava_lord]["sign"]

    sign_to_house = {v: int(k) for k, v in chart["houses"].items()}
    lord_house = sign_to_house[lord_sign]
    planets_in_bhava = [g for g, d in chart["grahas"].items() if sign_to_house[d["sign"]] == 11]

    strength = shadbala.get(bhava_lord, {}).get("TotalRupas", 0)
    strength_label = (
        "very strong" if strength >= 7 else
        "strong" if strength >= 5 else
        "moderate" if strength >= 3 else
        "weak" if strength >= 1.5 else
        "very weak"
    )

    interpretation = []

    interpretation.append(f"🪙 The 11th house falls in **{sign_in_11th}**, representing gains, income, ambitions, and social reach.")
    interpretation.append(f"👑 The 11th house lord is **{bhava_lord}**, placed in the **{lord_house}th house** in **{lord_sign}**.")
    interpretation.append(f"🔗 This connects earnings and wish-fulfillment with the affairs of the {lord_house}th house.")

    interpretation.append(f"📊 The 11th lord's strength is **{strength:.2f} Rupas**, categorized as **{strength_label}**.")

    if planets_in_bhava:
        for p in planets_in_bhava:
            if p in benefics:
                interpretation.append(f"💰 Benefic **{p}** in 11th house blesses strong networks, financial success, and fulfilled ambitions.")
            elif p in malefics:
                interpretation.append(f"⚠️ Malefic **{p}** in 11th house may delay income or bring strained friendships despite high goals.")
            else:
                interpretation.append(f"🔍 Presence of **{p}** in 11th house adds distinct flair to gains and social affiliations.")
    else:
        interpretation.append("📭 No planets in 11th house — income and desires rely mostly on the 11th lord's strength and placement.")

    return "\n".join(interpretation)
