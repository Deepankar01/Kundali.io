from shadbala.decorator import validate_shadbala


@validate_shadbala()
def detect_yava_yoga(chart, sign_occupancy, signs_order):
    lagna = chart["ascendant"]
    lagna_index = signs_order.index(lagna)
    sign_4 = signs_order[(lagna_index + 3) % 12]
    sign_7 = signs_order[(lagna_index + 6) % 12]
    sign_10 = signs_order[(lagna_index + 9) % 12]

    if (
        sign_occupancy[lagna] and
        sign_occupancy[sign_4] and
        sign_occupancy[sign_7] and
        sign_occupancy[sign_10]
    ):
        involved = (
            sign_occupancy[lagna] +
            sign_occupancy[sign_4] +
            sign_occupancy[sign_7] +
            sign_occupancy[sign_10]
        )
        return {
            "yoga_name": "Yava Yoga",
            "planets": involved
        }
    return None