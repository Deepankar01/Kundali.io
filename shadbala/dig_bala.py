# Signs and sign order
signs_order = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
               "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

# Dig Bala implementation
def calculate_dig_bala(chart):
    preferred_houses = {
        "Sun": 10,
        "Moon": 4,
        "Mars": 10,
        "Mercury": 1,
        "Jupiter": 1,
        "Venus": 4,
        "Saturn": 7
    }

    house_scores = {0: 60, 1: 30, 2: 15, 3: 0}

    dig_bala = {}
    house_signs = chart["houses"]

    sign_to_house = {}
    for h, sign in house_signs.items():
        sign_to_house[sign] = int(h)

    for graha in preferred_houses:
        planet_sign = chart['grahas'][graha]["sign"]
        planet_house = sign_to_house.get(planet_sign)
        preferred_house = preferred_houses[graha]

        if planet_house:
            offset = (planet_house - preferred_house) % 12
            if offset > 6:
                offset = 12 - offset
            virupas = house_scores.get(offset, 0)
        else:
            virupas = 0

        dig_bala[graha] = {
            "DigBalaVirupas": virupas,
            "DigBalaRupas": round(virupas / 60, 2)
        }

    return dig_bala