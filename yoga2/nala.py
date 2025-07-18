from shadbala.decorator import validate_shadbala


@validate_shadbala()
def detect_nala_yoga(chart):
    dual = {"Gemini", "Virgo", "Sagittarius", "Pisces"}
    non_luminaries = [g for g in chart["grahas"] if g not in ("Sun", "Moon")]
    if all(chart["grahas"][g]["sign"] in dual for g in non_luminaries):
        return {
            "yoga_name": "Nala Yoga",
            "planets": non_luminaries
        }
    return None
