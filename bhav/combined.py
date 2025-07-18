# Bundle all Bhava interpretations with strength
from bhav.bhav_10th import interpret_10th_bhava
from bhav.bhav_11th import interpret_11th_bhava
from bhav.bhav_12th import interpret_12th_bhava
from bhav.bhav_1st import interpret_lagna_bhava
from bhav.bhav_2nd import interpret_2nd_bhava
from bhav.bhav_3rd import interpret_3rd_bhava
from bhav.bhav_4th import interpret_4th_bhava
from bhav.bhav_5th import interpret_5th_bhava
from bhav.bhav_6th import interpret_6th_bhava
from bhav.bhav_7th import interpret_7th_bhava
from bhav.bhav_8th import interpret_8th_bhava
from bhav.bhav_9th import interpret_9th_bhava


def interpret_all_bhavas(chart, shadbala):
    bhava_functions = {
        1: interpret_lagna_bhava,
        2: interpret_2nd_bhava,
        3: interpret_3rd_bhava,
        4: interpret_4th_bhava,
        5: interpret_5th_bhava,
        6: interpret_6th_bhava,
        7: interpret_7th_bhava,
        8: interpret_8th_bhava,
        9: interpret_9th_bhava,
        10: interpret_10th_bhava,
        11: interpret_11th_bhava,
        12: interpret_12th_bhava,
    }

    # Map each house to its lord for Shadbala strength lookup
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

    result = {}

    for bhava_num, func in bhava_functions.items():
        sign = chart["houses"][str(bhava_num)]
        lord = bhava_lord_map[sign]
        strength = shadbala.get(lord, {}).get("TotalRupas", 0)
        interpretation = func(chart, shadbala)
        result[bhava_num] = {
            "BhavaSign": sign,
            "HouseLord": lord,
            "HouseLordStrength": round(strength, 2),
            "Interpretation": interpretation,
        }

    return result
