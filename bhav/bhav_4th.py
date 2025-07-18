# 4th Bhava interpretation (Home, Comfort, Mother, Real Estate)
def interpret_4th_bhava(chart, shadbala):
    sign_in_4th = chart["houses"]["4"]
    bhava_lord_map = {
        "Aries": "Mars", "Taurus": "Venus", "Gemini": "Mercury", "Cancer": "Moon",
        "Leo": "Sun", "Virgo": "Mercury", "Libra": "Venus", "Scorpio": "Mars",
        "Sagittarius": "Jupiter", "Capricorn": "Saturn", "Aquarius": "Saturn", "Pisces": "Jupiter"
    }
    benefics = ["Jupiter", "Venus", "Mercury", "Moon"]
    malefics = ["Saturn", "Mars", "Sun", "Rahu", "Ketu"]

    bhava_lord = bhava_lord_map[sign_in_4th]
    lord_sign = chart["grahas"][bhava_lord]["sign"]

    sign_to_house = {v: int(k) for k, v in chart["houses"].items()}
    lord_house = sign_to_house[lord_sign]
    planets_in_bhava = [g for g, d in chart["grahas"].items() if sign_to_house[d["sign"]] == 4]

    strength = shadbala.get(bhava_lord, {}).get("TotalRupas", 0)
    strength_label = (
        "very strong" if strength >= 7 else
        "strong" if strength >= 5 else
        "moderate" if strength >= 3 else
        "weak" if strength >= 1.5 else
        "very weak"
    )

    interpretation = []

    interpretation.append(f"🏡 The 4th house falls in **{sign_in_4th}**, influencing home life, emotions, and maternal connections.")
    interpretation.append(f"👑 The 4th house lord is **{bhava_lord}**, placed in the **{lord_house}th house** in **{lord_sign}**.")
    interpretation.append(f"🔗 This shows how emotional well-being and domestic life are influenced by the matters of the {lord_house}th house.")

    interpretation.append(f"📊 The 4th lord's strength is **{strength:.2f} Rupas**, categorized as **{strength_label}**.")

    if planets_in_bhava:
        for p in planets_in_bhava:
            if p in benefics:
                interpretation.append(f"💖 Benefic **{p}** in 4th house brings domestic happiness, maternal blessings, and property comforts.")
            elif p in malefics:
                interpretation.append(f"⚠️ Malefic **{p}** in 4th house may disturb peace at home, cause disputes over property or stress.")
            else:
                interpretation.append(f"🔍 Presence of **{p}** in 4th house has unique effects on emotional stability and real estate matters.")
    else:
        interpretation.append("📭 No planets in 4th house — focus depends on strength and condition of the house lord.")

    return "\n".join(interpretation)
