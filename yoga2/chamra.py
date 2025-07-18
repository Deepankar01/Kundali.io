from shadbala.decorator import validate_shadbala


@validate_shadbala()
def detect_chamara_yoga(chart, signs_order):
    lagna = chart["ascendant"]
    lagna_index = signs_order.index(lagna)
    kendras_from_lagna = {
        lagna,
        signs_order[(lagna_index + 3) % 12],
        signs_order[(lagna_index + 6) % 12],
        signs_order[(lagna_index + 9) % 12],
    }

    exalted = {"Mercury": "Virgo", "Jupiter": "Cancer"}
    own_signs = {"Mercury": {"Gemini", "Virgo"}, "Jupiter": {"Sagittarius", "Pisces"}}

    jup_sign = chart["grahas"]["Jupiter"]["sign"]
    merc_sign = chart["grahas"]["Mercury"]["sign"]

    yogas = []
    if jup_sign in kendras_from_lagna and (
        jup_sign in own_signs["Jupiter"] or jup_sign == exalted["Jupiter"]
    ):
        yogas.append({
            "yoga_name": "Chamara Yoga",
            "planets": ["Jupiter"]
        })
    if merc_sign in kendras_from_lagna and (
        merc_sign in own_signs["Mercury"] or merc_sign == exalted["Mercury"]
    ):
        yogas.append({
            "yoga_name": "Chamara Yoga",
            "planets": ["Mercury"]
        })

    return yogas if yogas else None