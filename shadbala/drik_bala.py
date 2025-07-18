# Full Drik Bala calculation
def calculate_drik_bala(chart):
    # Aspect rules
    special_aspects = {
        "Mars": [120, 180, 210],
        "Jupiter": [150, 180, 240],
        "Saturn": [90, 180, 270]
    }

    # Default 7th house aspect for all planets
    all_aspect_angles = {
        "Sun": [180], "Moon": [180], "Mercury": [180], "Venus": [180],
        "Mars": special_aspects["Mars"],
        "Jupiter": special_aspects["Jupiter"],
        "Saturn": special_aspects["Saturn"]
    }

    # Benefics and Malefics
    benefics = ["Jupiter", "Venus", "Mercury", "Moon"]
    malefics = ["Saturn", "Mars", "Sun"]

    # Longitudes
    signs_order = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
                   "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
    longitudes = {
        p: signs_order.index(data["sign"]) * 30 + data["degree"]
        for p, data in chart["grahas"].items()
        if p in all_aspect_angles
    }

    drik_bala = {p: 0 for p in longitudes}  # Net strength

    for giver in longitudes:
        giver_lon = longitudes[giver]
        aspect_angles = all_aspect_angles[giver]
        for receiver in longitudes:
            if giver == receiver:
                continue
            recv_lon = longitudes[receiver]
            delta = (recv_lon - giver_lon + 360) % 360

            # Check if delta matches any defined aspect angle (±15° window)
            matching_strength = 0
            for asp in aspect_angles:
                diff = abs(delta - asp)
                if diff <= 15:
                    matching_strength = round(60 * (1 - diff / 15), 2)  # Linear fall-off
                    break

            # Sign (+) or (-)
            if giver in benefics:
                drik_bala[receiver] += matching_strength
            elif giver in malefics:
                drik_bala[receiver] -= matching_strength

    # Format output
    drik_bala_output = {
        p: {
            "DrikBalaVirupas": round(score, 2),
            "DrikBalaRupas": round(score / 60, 2)
        } for p, score in drik_bala.items()
    }

    return drik_bala_output
