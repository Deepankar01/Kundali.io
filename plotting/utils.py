def prepare_planets_by_house(chart):
    # Reverse lookup: map sign to house
    sign_to_house = {v: k for k, v in chart["houses"].items()}

    # Prepare planet positions per house
    planets_by_house = {str(i): [] for i in range(1, 13)}
    for graha, data in chart["grahas"].items():
        sign = data["sign"]
        house = sign_to_house.get(sign)
        if house:
            planets_by_house[house].append(graha)

    # Add ASC marker
    asc_house = [k for k, v in chart["houses"].items() if v == chart["ascendant"]][0]
    planets_by_house[asc_house].insert(0, 'ASC')
    return planets_by_house
