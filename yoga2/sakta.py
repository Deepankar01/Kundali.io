from shadbala.decorator import validate_shadbala


@validate_shadbala()
def detect_sakata_yoga(chart, signs_order):
    jup_sign = chart["grahas"]["Jupiter"]["sign"]
    moon_sign = chart["grahas"]["Moon"]["sign"]
    jup_index = signs_order.index(jup_sign)
    moon_index = signs_order.index(moon_sign)
    if abs(jup_index - moon_index) % 12 == 6:
        return {
            "yoga_name": "Sakata Yoga",
            "planets": ["Jupiter", "Moon"]
        }
    return None