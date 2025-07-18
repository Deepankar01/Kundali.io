# 12th Bhava interpretation (Losses, Isolation, Moksha, Expenses)
def interpret_12th_bhava(chart, shadbala):
    sign_in_12th = chart["houses"]["12"]
    bhava_lord_map = {
        "Aries": "Mars", "Taurus": "Venus", "Gemini": "Mercury", "Cancer": "Moon",
        "Leo": "Sun", "Virgo": "Mercury", "Libra": "Venus", "Scorpio": "Mars",
        "Sagittarius": "Jupiter", "Capricorn": "Saturn", "Aquarius": "Saturn", "Pisces": "Jupiter"
    }
    benefics = ["Jupiter", "Venus", "Mercury", "Moon"]
    malefics = ["Saturn", "Mars", "Sun", "Rahu", "Ketu"]

    bhava_lord = bhava_lord_map[sign_in_12th]
    lord_sign = chart["grahas"][bhava_lord]["sign"]

    sign_to_house = {v: int(k) for k, v in chart["houses"].items()}
    lord_house = sign_to_house[lord_sign]
    planets_in_bhava = [g for g, d in chart["grahas"].items() if sign_to_house[d["sign"]] == 12]

    strength = shadbala.get(bhava_lord, {}).get("TotalRupas", 0)
    strength_label = (
        "very strong" if strength >= 7 else
        "strong" if strength >= 5 else
        "moderate" if strength >= 3 else
        "weak" if strength >= 1.5 else
        "very weak"
    )

    interpretation = []

    interpretation.append(f"🧘 The 12th house falls in **{sign_in_12th}**, ruling isolation, expenses, spiritual liberation, and distant lands.")
    interpretation.append(f"👑 The 12th house lord is **{bhava_lord}**, placed in the **{lord_house}th house** in **{lord_sign}**.")
    interpretation.append(f"🔗 This connects inner retreat, loss, or liberation with themes of the {lord_house}th house.")

    interpretation.append(f"📊 The 12th lord's strength is **{strength:.2f} Rupas**, categorized as **{strength_label}**.")

    if planets_in_bhava:
        for p in planets_in_bhava:
            if p in benefics:
                interpretation.append(f"🕊️ Benefic **{p}** in 12th house supports spiritual insight, charitable acts, or fruitful foreign ventures.")
            elif p in malefics:
                interpretation.append(f"⚠️ Malefic **{p}** in 12th house may lead to losses, hidden enemies, or escapist tendencies.")
            else:
                interpretation.append(f"🔍 Presence of **{p}** in 12th house uniquely shapes your journey of retreat, expenses, or moksha.")
    else:
        interpretation.append("📭 No planets in 12th house — impact comes through strength and placement of the 12th lord.")

    return "\n".join(interpretation)
