# Interpret Lagna Bhava (1st house)
def interpret_lagna_bhava(chart, shadbala):
    sign_in_lagna = chart["houses"]["1"]
    lagna_lord_map = {
        "Aries": "Mars", "Taurus": "Venus", "Gemini": "Mercury", "Cancer": "Moon",
        "Leo": "Sun", "Virgo": "Mercury", "Libra": "Venus", "Scorpio": "Mars",
        "Sagittarius": "Jupiter", "Capricorn": "Saturn", "Aquarius": "Saturn", "Pisces": "Jupiter"
    }
    benefics = ["Jupiter", "Venus", "Mercury", "Moon"]
    malefics = ["Saturn", "Mars", "Sun", "Rahu", "Ketu"]

    lagna_lord = lagna_lord_map[sign_in_lagna]
    lord_sign = chart["grahas"][lagna_lord]["sign"]

    sign_to_house = {v: int(k) for k, v in chart["houses"].items()}
    lord_house = sign_to_house[lord_sign]
    planets_in_lagna = [g for g, d in chart["grahas"].items() if sign_to_house[d["sign"]] == 1]

    strength = shadbala.get(lagna_lord, {}).get("TotalRupas", 0)
    strength_label = (
        "very strong" if strength >= 7 else
        "strong" if strength >= 5 else
        "moderate" if strength >= 3 else
        "weak" if strength >= 1.5 else
        "very weak"
    )

    interpretation = []

    interpretation.append(f"The Ascendant sign is **{sign_in_lagna}**, indicating a personality that is shaped by its qualities.")
    interpretation.append(f"The Lagna lord is **{lagna_lord}**, placed in the **{lord_house}th house** in **{lord_sign}**.")
    interpretation.append(f"This suggests influence of the {lord_house}th house (e.g. dharma, fortune, etc.) on self-expression.")

    interpretation.append(f"The Lagna lord's strength is **{strength:.2f} Rupas**, categorized as **{strength_label}**.")

    if planets_in_lagna:
        for p in planets_in_lagna:
            if p in benefics:
                interpretation.append(f"Presence of benefic **{p}** in Lagna enhances vitality, fame, and charm.")
            elif p in malefics:
                interpretation.append(f"Presence of malefic **{p}** in Lagna may bring challenges to health, confidence, or appearance.")
            else:
                interpretation.append(f"Presence of **{p}** in Lagna influences self-identity in unique ways.")
    else:
        interpretation.append("There are no planets in Lagna, so the self-image is less altered by planetary influences.")

    return "\n".join(interpretation)
