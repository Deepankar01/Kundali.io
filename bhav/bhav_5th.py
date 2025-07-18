# 5th Bhava interpretation (Children, Intelligence, Creativity)
def interpret_5th_bhava(chart, shadbala):
    sign_in_5th = chart["houses"]["5"]
    bhava_lord_map = {
        "Aries": "Mars", "Taurus": "Venus", "Gemini": "Mercury", "Cancer": "Moon",
        "Leo": "Sun", "Virgo": "Mercury", "Libra": "Venus", "Scorpio": "Mars",
        "Sagittarius": "Jupiter", "Capricorn": "Saturn", "Aquarius": "Saturn", "Pisces": "Jupiter"
    }
    benefics = ["Jupiter", "Venus", "Mercury", "Moon"]
    malefics = ["Saturn", "Mars", "Sun", "Rahu", "Ketu"]

    bhava_lord = bhava_lord_map[sign_in_5th]
    lord_sign = chart["grahas"][bhava_lord]["sign"]

    sign_to_house = {v: int(k) for k, v in chart["houses"].items()}
    lord_house = sign_to_house[lord_sign]
    planets_in_bhava = [g for g, d in chart["grahas"].items() if sign_to_house[d["sign"]] == 5]

    strength = shadbala.get(bhava_lord, {}).get("TotalRupas", 0)
    strength_label = (
        "very strong" if strength >= 7 else
        "strong" if strength >= 5 else
        "moderate" if strength >= 3 else
        "weak" if strength >= 1.5 else
        "very weak"
    )

    interpretation = []

    interpretation.append(f"🎓 The 5th house falls in **{sign_in_5th}**, affecting intelligence, creativity, and children.")
    interpretation.append(f"👑 The 5th house lord is **{bhava_lord}**, placed in the **{lord_house}th house** in **{lord_sign}**.")
    interpretation.append(f"🔗 This placement links education, romance, or progeny to the affairs of the {lord_house}th house.")

    interpretation.append(f"📊 The 5th lord's strength is **{strength:.2f} Rupas**, categorized as **{strength_label}**.")

    if planets_in_bhava:
        for p in planets_in_bhava:
            if p in benefics:
                interpretation.append(f"🌟 Benefic **{p}** in 5th house supports creativity, learning, love life, and children’s well-being.")
            elif p in malefics:
                interpretation.append(f"⚠️ Malefic **{p}** in 5th house may indicate challenges in education, romance, or offspring.")
            else:
                interpretation.append(f"🔍 Presence of **{p}** in 5th house brings unique influences on intellect and self-expression.")
    else:
        interpretation.append("📭 No planets in 5th house — primary focus is on the lord's strength and condition.")

    return "\n".join(interpretation)
