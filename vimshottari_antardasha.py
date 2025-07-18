def vimshottari_antardasha(mahadasa_sequence):
    """
    For each Mahadasha, calculate its Antardasha periods based on BPHS Vimshottari rules.
    Returns a dict with each Mahadasha containing sub-periods.
    """

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

    planets = list(dasha_years.keys())
    antardasha_result = []

    for maha in mahadasa_sequence:
        maha_lord = maha["lord"]
        maha_years = maha["years"]

        antardashas = []
        total = 0
        for antar_lord in planets:
            proportion = dasha_years[antar_lord] / 120
            antar_years = round(maha_years * proportion, 2)
            antardashas.append({
                "lord": antar_lord,
                "years": antar_years
            })
            total += antar_years

        # Normalize if total overshoots due to rounding
        if total > maha_years:
            diff = total - maha_years
            antardashas[-1]["years"] -= diff

        antardasha_result.append({
            "mahadasha_lord": maha_lord,
            "mahadasha_years": maha_years,
            "partial": maha.get("partial", False),
            "antardashas": antardashas
        })

    return antardasha_result
