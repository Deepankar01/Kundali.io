from shadbala.decorator import validate_shadbala


@validate_shadbala()
def detect_gada_yoga(chart, sign_occupancy):
    gada_zones = [("Aries", "Cancer"), ("Libra", "Capricorn")]
    for zone1, zone2 in gada_zones:
        if sign_occupancy[zone1] and sign_occupancy[zone2]:
            return {
                "yoga_name": "Gada Yoga",
                "planets": sign_occupancy[zone1] + sign_occupancy[zone2]
            }
    return None