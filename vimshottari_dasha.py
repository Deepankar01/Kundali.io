def vimshottari_dasha(chart):
    """
    Calculate Vimshottari Mahadasha sequence based on BPHS rules.
    Input: chart from generate_rasi_chart()
    Output: list of Mahadasha periods with years and balance from birth
    """

    # Nakshatra lords in order of zodiac (27 Nakshatras)
    nakshatra_lords = [
        "Ketu", "Venus", "Sun", "Moon", "Mars", "Rahu", "Jupiter", "Saturn", "Mercury"
    ] * 3  # Repeat to cover all 27

    # Vimshottari Dasha durations
    dasha_years = {
        "Ketu": 7,
        "Venus": 20,
        "Sun": 6,
        "Moon": 10,
        "Mars": 7,
        "Rahu": 18,
        "Jupiter": 16,
        "Saturn": 19,
        "Mercury": 17
    }

    # Each Nakshatra is 13°20′ = 13.333... degrees
    nakshatra_size = 13 + 20/60  # = 13.333...

    # Moon's sidereal longitude
    moon_sign = chart['grahas']['Moon']['sign']
    moon_deg = chart['grahas']['Moon']['degree']
    signs_order = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
                   "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]
    sign_index = signs_order.index(moon_sign)
    moon_longitude = sign_index * 30 + moon_deg

    # Nakshatra index
    nak_index = int(moon_longitude // nakshatra_size)
    nak_fraction = (moon_longitude % nakshatra_size) / nakshatra_size

    current_lord = nakshatra_lords[nak_index]
    total_years = dasha_years[current_lord]
    balance_years = (1 - nak_fraction) * total_years

    # Generate 120 year cycle starting from current lord
    sequence = []
    current_index = list(dasha_years.keys()).index(current_lord)
    remaining = balance_years
    sequence.append({"lord": current_lord, "years": round(balance_years, 2), "partial": True})

    total_lived = balance_years
    for i in range(1, len(dasha_years)):
        lord = list(dasha_years.keys())[(current_index + i) % 9]
        years = dasha_years[lord]
        if total_lived + years > 120:
            years = round(120 - total_lived, 2)
        sequence.append({"lord": lord, "years": years, "partial": False})
        total_lived += years
        if total_lived >= 120:
            break

    return sequence
