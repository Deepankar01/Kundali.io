from shadbala.decorator import validate_shadbala


@validate_shadbala()
def detect_sunapha_anapha_yoga(chart, sign_occupancy, signs_order):
    moon_sign = chart["grahas"]["Moon"]["sign"]
    moon_pos = signs_order.index(moon_sign)
    surrounding = set()
    for offset in [11, 1]:
        neighbor_sign = signs_order[(moon_pos + offset) % 12]
        surrounding.update(sign_occupancy[neighbor_sign])
    benefics = {"Mercury", "Venus", "Jupiter"}
    if surrounding and all(g in benefics for g in surrounding):
        return {"yoga_name": "Sunapha/Anapha Yoga", "planets": list(surrounding)}
    return None
