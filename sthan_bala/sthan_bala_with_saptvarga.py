# Update Sthana Bala function to include Saptavargaja Bala
from saptavargaja.saptavargaja_bala import calculate_saptavargaja_bala


def calculate_sthana_bala_with_saptavarga(chart):
    exaltation_points = {
        "Sun": ("Aries", 10),
        "Moon": ("Taurus", 3),
        "Mars": ("Capricorn", 28),
        "Mercury": ("Virgo", 15),
        "Jupiter": ("Cancer", 5),
        "Venus": ("Pisces", 27),
        "Saturn": ("Libra", 20)
    }

    planet_genders = {
        "Sun": "male", "Moon": "female", "Mars": "male", "Mercury": "eunuch",
        "Jupiter": "male", "Venus": "female", "Saturn": "eunuch"
    }

    signs_order = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
                   "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

    saptavarga_scores = calculate_saptavargaja_bala(chart)
    sthana_bala = {}

    for graha in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]:
        info = chart['grahas'][graha]
        rasi = info["sign"]
        deg = info["degree"]
        sign_index = signs_order.index(rasi)
        abs_long = sign_index * 30 + deg

        # 1. Uchcha Bala
        exalt_sign, exalt_deg = exaltation_points[graha]
        exalt_index = signs_order.index(exalt_sign)
        exalt_abs = exalt_index * 30 + exalt_deg
        diff = (abs_long - (exalt_abs - 180)) % 360
        if diff > 180:
            diff = 360 - diff
        uchcha_bala = round(diff / 3, 2)

        # 2. Kendradi Bala
        bhava_sign = chart["houses"]
        graha_house = next((int(house) for house, sign in bhava_sign.items() if sign == rasi), None)
        if graha_house in [1, 4, 7, 10]:
            kendradi = 60
        elif graha_house in [2, 5, 8, 11]:
            kendradi = 30
        else:
            kendradi = 15

        # 3. Oja-Yugma Bala
        is_even = (sign_index + 1) % 2 == 0
        if graha in ["Venus", "Moon"]:
            ojyugma = 15 if is_even else 0
        else:
            ojyugma = 15 if not is_even else 0

        # 4. Drekkana Bala
        decan = int(deg // 10) + 1
        gender = planet_genders[graha]
        if (gender == "male" and decan == 1) or (gender == "female" and decan == 2) or (gender == "eunuch" and decan == 3):
            drekkana = 15
        else:
            drekkana = 0

        # 5. Saptavargaja Bala
        saptavarga = saptavarga_scores[graha]["TotalVirupas"]

        total = uchcha_bala + kendradi + ojyugma + drekkana + saptavarga
        sthana_bala[graha] = {
            "UchchaBala": uchcha_bala,
            "KendradiBala": kendradi,
            "OjaYugmaBala": ojyugma,
            "DrekkanaBala": drekkana,
            "SaptavargajaBala": saptavarga,
            "TotalVirupas": round(total, 2),
            "TotalRupas": round(total / 60, 2)
        }

    return sthana_bala

# Re-run full sthana bala
# full_sthana_bala = calculate_sthana_bala_with_saptavarga(chart)
# tools.display_dataframe_to_user(name="Full Sthana Bala (with Saptavargaja)", dataframe=pd.DataFrame(full_sthana_bala).T)
