# 10th Bhava interpretation (Career, Status, Profession)
def interpret_10th_bhava(chart, shadbala):
    sign_in_10th = chart["houses"]["10"]
    bhava_lord_map = {
        "Aries": "Mars",
        "Taurus": "Venus",
        "Gemini": "Mercury",
        "Cancer": "Moon",
        "Leo": "Sun",
        "Virgo": "Mercury",
        "Libra": "Venus",
        "Scorpio": "Mars",
        "Sagittarius": "Jupiter",
        "Capricorn": "Saturn",
        "Aquarius": "Saturn",
        "Pisces": "Jupiter",
    }
    benefics = ["Jupiter", "Venus", "Mercury", "Moon"]
    malefics = ["Saturn", "Mars", "Sun", "Rahu", "Ketu"]

    bhava_lord = bhava_lord_map[sign_in_10th]
    lord_sign = chart["grahas"][bhava_lord]["sign"]

    sign_to_house = {v: int(k) for k, v in chart["houses"].items()}
    lord_house = sign_to_house[lord_sign]
    planets_in_bhava = [g for g, d in chart["grahas"].items() if sign_to_house[d["sign"]] == 10]

    strength = shadbala.get(bhava_lord, {}).get("TotalRupas", 0)
    strength_label = (
        "very strong"
        if strength >= 7
        else (
            "strong"
            if strength >= 5
            else "moderate" if strength >= 3 else "weak" if strength >= 1.5 else "very weak"
        )
    )

    interpretation = []

    interpretation.append(
        f"🏛️ The 10th house is in **{sign_in_10th}**, governing karma, profession, and reputation."
    )
    interpretation.append(
        f"👑 The 10th house lord is **{bhava_lord}**, placed in the **{lord_house}th house** in **{lord_sign}**."
    )
    interpretation.append(
        f"🔗 This ties your career and actions to the affairs of the {lord_house}th house."
    )

    interpretation.append(
        f"📊 The 10th lord's strength is **{strength:.2f} Rupas**, categorized as **{strength_label}**."
    )

    if planets_in_bhava:
        for p in planets_in_bhava:
            if p in benefics:
                interpretation.append(
                    f"📈 Benefic **{p}** in 10th house supports a strong reputation, public recognition, and leadership."
                )
            elif p in malefics:
                interpretation.append(
                    f"⚠️ Malefic **{p}** in 10th house may cause delays, stress, or instability in career path."
                )
            else:
                interpretation.append(
                    f"🔍 Presence of **{p}** in 10th house influences karmic pursuits and professional uniqueness."
                )
    else:
        interpretation.append(
            "📭 No planets in 10th house — professional success depends primarily on the 10th lord’s strength and associations."
        )

    return "\n".join(interpretation)
