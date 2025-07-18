from shadbala.decorator import validate_shadbala


@validate_shadbala()
def detect_daama_yoga(chart):
    occupied_signs = {data["sign"] for data in chart["grahas"].values()}
    if len(occupied_signs) == 6:
        return {"yoga_name": "Daama Yoga", "planets": list(chart["grahas"].keys())}
    return None
