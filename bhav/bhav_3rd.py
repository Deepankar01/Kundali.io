# 3rd Bhava interpretation (Courage, Siblings, Communication)
def interpret_3rd_bhava(chart, shadbala):
    sign_in_3rd = chart["houses"]["3"]
    bhava_lord_map = {
        "Aries": "Mars", "Taurus": "Venus", "Gemini": "Mercury", "Cancer": "Moon",
        "Leo": "Sun", "Virgo": "Mercury", "Libra": "Venus", "Scorpio": "Mars",
        "Sagittarius": "Jupiter", "Capricorn": "Saturn", "Aquarius": "Saturn", "Pisces": "Jupiter"
    }
    benefics = ["Jupiter", "Venus", "Mercury", "Moon"]
    malefics = ["Saturn", "Mars", "Sun", "Rahu", "Ketu"]

    bhava_lord = bhava_lord_map[sign_in_3rd]
    lord_sign = chart["grahas"][bhava_lord]["sign"]

    sign_to_house = {v: int(k) for k, v in chart["houses"].items()}
    lord_house = sign_to_house[lord_sign]
    planets_in_bhava = [g for g, d in chart["grahas"].items() if sign_to_house[d["sign"]] == 3]

    strength = shadbala.get(bhava_lord, {}).get("TotalRupas", 0)
    strength_label = (
        "very strong" if strength >= 7 else
        "strong" if strength >= 5 else
        "moderate" if strength >= 3 else
        "weak" if strength >= 1.5 else
        "very weak"
    )

    interpretation = []

    interpretation.append(f"🏠 The 3rd house has **{sign_in_3rd}**, influencing courage, communication, and siblings with that sign's qualities.")
    interpretation.append(f"👑 The 3rd house lord is **{bhava_lord}**, placed in the **{lord_house}th house** in **{lord_sign}**.")
    interpretation.append(f"🔗 This links self-effort and communication with the matters of the {lord_house}th house.")

    interpretation.append(f"📊 The 3rd lord's strength is **{strength:.2f} Rupas**, categorized as **{strength_label}**.")

    if planets_in_bhava:
        for p in planets_in_bhava:
            if p in benefics:
                interpretation.append(f"💬 Benefic **{p}** in 3rd house enhances communication skills, artistic talents, and sibling harmony.")
            elif p in malefics:
                interpretation.append(f"⚠️ Malefic **{p}** in 3rd house may cause sibling disputes, risky behavior, or anxiety in expression.")
            else:
                interpretation.append(f"🧭 Presence of **{p}** in 3rd house brings unique influence on communication and willpower.")
    else:
        interpretation.append("📭 No planets in 3rd house — interpretation depends mainly on the strength and dignity of its lord.")

    return "\n".join(interpretation)
