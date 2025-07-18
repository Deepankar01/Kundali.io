# 6th Bhava interpretation (Enemies, Debts, Diseases, Service)
def interpret_6th_bhava(chart, shadbala):
    sign_in_6th = chart["houses"]["6"]
    bhava_lord_map = {
        "Aries": "Mars", "Taurus": "Venus", "Gemini": "Mercury", "Cancer": "Moon",
        "Leo": "Sun", "Virgo": "Mercury", "Libra": "Venus", "Scorpio": "Mars",
        "Sagittarius": "Jupiter", "Capricorn": "Saturn", "Aquarius": "Saturn", "Pisces": "Jupiter"
    }
    benefics = ["Jupiter", "Venus", "Mercury", "Moon"]
    malefics = ["Saturn", "Mars", "Sun", "Rahu", "Ketu"]

    bhava_lord = bhava_lord_map[sign_in_6th]
    lord_sign = chart["grahas"][bhava_lord]["sign"]

    sign_to_house = {v: int(k) for k, v in chart["houses"].items()}
    lord_house = sign_to_house[lord_sign]
    planets_in_bhava = [g for g, d in chart["grahas"].items() if sign_to_house[d["sign"]] == 6]

    strength = shadbala.get(bhava_lord, {}).get("TotalRupas", 0)
    strength_label = (
        "very strong" if strength >= 7 else
        "strong" if strength >= 5 else
        "moderate" if strength >= 3 else
        "weak" if strength >= 1.5 else
        "very weak"
    )

    interpretation = []

    interpretation.append(f"🛡️ The 6th house falls in **{sign_in_6th}**, governing enemies, debts, diseases, and competition.")
    interpretation.append(f"👑 The 6th house lord is **{bhava_lord}**, placed in the **{lord_house}th house** in **{lord_sign}**.")
    interpretation.append(f"🔗 This connects service, health, and conflict resolution to the matters of the {lord_house}th house.")

    interpretation.append(f"📊 The 6th lord's strength is **{strength:.2f} Rupas**, categorized as **{strength_label}**.")

    if planets_in_bhava:
        for p in planets_in_bhava:
            if p in benefics:
                interpretation.append(f"🩺 Benefic **{p}** in 6th house may help overcome obstacles, improve service attitude, and aid healing.")
            elif p in malefics:
                interpretation.append(f"⚠️ Malefic **{p}** in 6th house can increase conflicts, chronic issues, or debts—but also gives fighting spirit.")
            else:
                interpretation.append(f"🔍 Presence of **{p}** in 6th house gives unique impact on service, resilience, and enemies.")
    else:
        interpretation.append("📭 No planets in 6th house — outcomes depend heavily on lord’s strength and house connections.")

    return "\n".join(interpretation)
