from shadbala.decorator import validate_shadbala


@validate_shadbala()
def detect_vajra_yoga(chart, sign_occupancy, signs_order):
    lagna = chart["ascendant"]
    lagna_index = signs_order.index(lagna)
    sign_4 = signs_order[(lagna_index + 3) % 12]
    sign_7 = signs_order[(lagna_index + 6) % 12]
    sign_10 = signs_order[(lagna_index + 9) % 12]

    benefics = {"Mercury", "Venus", "Jupiter"}
    malefics = {"Sun", "Mars", "Saturn"}

    if (
        any(p in benefics for p in sign_occupancy[lagna]) and
        any(p in benefics for p in sign_occupancy[sign_7]) and
        any(p in malefics for p in sign_occupancy[sign_4]) and
        any(p in malefics for p in sign_occupancy[sign_10])
    ):
        involved = (
            sign_occupancy[lagna] +
            sign_occupancy[sign_4] +
            sign_occupancy[sign_7] +
            sign_occupancy[sign_10]
        )
        return {
            "yoga_name": "Vajra Yoga",
            "planets": involved
        }
    return None
