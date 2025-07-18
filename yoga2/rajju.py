from shadbala.decorator import validate_shadbala


@validate_shadbala()
def detect_rajju_yoga(chart):
    movable = {"Aries", "Cancer", "Libra", "Capricorn"}
    non_luminaries = [g for g in chart["grahas"] if g not in ("Sun", "Moon")]
    if all(chart["grahas"][g]["sign"] in movable for g in non_luminaries):
        return {
            "yoga_name": "Rajju Yoga",
            "planets": non_luminaries
        }
    return None