# 9th Bhava interpretation (Fortune, Higher Learning, Dharma)
def interpret_9th_bhava(chart, shadbala):
    sign_in_9th = chart["houses"]["9"]
    bhava_lord_map = {
        "Aries": "Mars", "Taurus": "Venus", "Gemini": "Mercury", "Cancer": "Moon",
        "Leo": "Sun", "Virgo": "Mercury", "Libra": "Venus", "Scorpio": "Mars",
        "Sagittarius": "Jupiter", "Capricorn": "Saturn", "Aquarius": "Saturn", "Pisces": "Jupiter"
    }
    benefics = ["Jupiter", "Venus", "Mercury", "Moon"]
    malefics = ["Saturn", "Mars", "Sun", "Rahu", "Ketu"]

    bhava_lord = bhava_lord_map[sign_in_9th]
    lord_sign = chart["grahas"][bhava_lord]["sign"]

    sign_to_house = {v: int(k) for k, v in chart["houses"].items()}
    lord_house = sign_to_house[lord_sign]
    planets_in_bhava = [g for g, d in chart["grahas"].items() if sign_to_house[d["sign"]] == 9]

    strength = shadbala.get(bhava_lord, {}).get("TotalRupas", 0)
    strength_label = (
        "very strong" if strength >= 7 else
        "strong" if strength >= 5 else
        "moderate" if strength >= 3 else
        "weak" if strength >= 1.5 else
        "very weak"
    )

    interpretation = []

    interpretation.append(f"🕉️ The 9th house falls in **{sign_in_9th}**, influencing dharma, fortune, father, and higher wisdom.")
    interpretation.append(f"👑 The 9th house lord is **{bhava_lord}**, placed in the **{lord_house}th house** in **{lord_sign}**.")
    interpretation.append(f"🔗 This connects fortune, beliefs, or long journeys with matters of the {lord_house}th house.")

    interpretation.append(f"📊 The 9th lord's strength is **{strength:.2f} Rupas**, categorized as **{strength_label}**.")

    if planets_in_bhava:
        for p in planets_in_bhava:
            if p in benefics:
                interpretation.append(f"📖 Benefic **{p}** in 9th house blesses wisdom, prosperity, and guidance from father/mentors.")
            elif p in malefics:
                interpretation.append(f"⚠️ Malefic **{p}** in 9th house may bring unconventional beliefs, strained fatherly bonds, or faith struggles.")
            else:
                interpretation.append(f"🔍 Presence of **{p}** in 9th house adds a unique flavor to your fortune, travels, or philosophical path.")
    else:
        interpretation.append("📭 No planets in 9th house — fortune and dharma depend mainly on the strength and dignity of its lord.")

    return "\n".join(interpretation)
