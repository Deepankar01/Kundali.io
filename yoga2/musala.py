from shadbala.decorator import validate_shadbala


@validate_shadbala()
def detect_musala_yoga(chart):
    fixed = {"Taurus", "Leo", "Scorpio", "Aquarius"}
    non_luminaries = [g for g in chart["grahas"] if g not in ("Sun", "Moon")]
    if all(chart["grahas"][g]["sign"] in fixed for g in non_luminaries):
        return {
            "yoga_name": "Musala Yoga",
            "planets": non_luminaries
        }
    return None