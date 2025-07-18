# Add one more: Gajakesari Yoga
from shadbala.decorator import validate_shadbala


@validate_shadbala()
def detect_gajakesari_yoga(chart, signs_order):
    jup_sign = chart["grahas"]["Jupiter"]["sign"]
    moon_sign = chart["grahas"]["Moon"]["sign"]
    moon_index = signs_order.index(moon_sign)
    kendras_from_moon = {signs_order[(moon_index + offset) % 12] for offset in [0, 3, 6, 9]}
    if jup_sign in kendras_from_moon:
        return {"yoga_name": "Gajakesari Yoga", "planets": ["Moon", "Jupiter"]}
    return None
