# Re-import necessary modules after code execution reset
import swisseph as swe
# Reset sidereal mode for BPHS
swe.set_sid_mode(swe.SIDM_LAHIRI)

# Define bhava interpretation function for 2nd house
def interpret_2nd_bhava(chart, shadbala):
    sign_in_2nd = chart["houses"]["2"]
    bhava_lord_map = {
        "Aries": "Mars", "Taurus": "Venus", "Gemini": "Mercury", "Cancer": "Moon",
        "Leo": "Sun", "Virgo": "Mercury", "Libra": "Venus", "Scorpio": "Mars",
        "Sagittarius": "Jupiter", "Capricorn": "Saturn", "Aquarius": "Saturn", "Pisces": "Jupiter"
    }
    benefics = ["Jupiter", "Venus", "Mercury", "Moon"]
    malefics = ["Saturn", "Mars", "Sun", "Rahu", "Ketu"]

    bhava_lord = bhava_lord_map[sign_in_2nd]
    lord_sign = chart["grahas"][bhava_lord]["sign"]

    sign_to_house = {v: int(k) for k, v in chart["houses"].items()}
    lord_house = sign_to_house[lord_sign]
    planets_in_bhava = [g for g, d in chart["grahas"].items() if sign_to_house[d["sign"]] == 2]

    strength = shadbala.get(bhava_lord, {}).get("TotalRupas", 0)
    strength_label = (
        "very strong" if strength >= 7 else
        "strong" if strength >= 5 else
        "moderate" if strength >= 3 else
        "weak" if strength >= 1.5 else
        "very weak"
    )

    interpretation = []

    interpretation.append(f"📍 The 2nd house is occupied by **{sign_in_2nd}**, influencing wealth, speech, and family with that sign's nature.")
    interpretation.append(f"👑 The 2nd house lord is **{bhava_lord}**, placed in the **{lord_house}th house** in **{lord_sign}**.")
    interpretation.append(f"🧭 This suggests a connection between wealth/family and the matters of the {lord_house}th house.")

    interpretation.append(f"📊 The 2nd lord's strength is **{strength:.2f} Rupas**, categorized as **{strength_label}**.")

    if planets_in_bhava:
        for p in planets_in_bhava:
            if p in benefics:
                interpretation.append(f"🪙 Benefic **{p}** in 2nd house supports good speech, stable income, and harmonious family ties.")
            elif p in malefics:
                interpretation.append(f"⚠️ Malefic **{p}** in 2nd house may cause strained speech, financial ups & downs, or family tensions.")
            else:
                interpretation.append(f"🔍 Presence of **{p}** in 2nd house uniquely influences wealth and values.")
    else:
        interpretation.append("📭 No planets in 2nd house — effects depend more on the strength and dignity of its lord.")

    return "\n".join(interpretation)
