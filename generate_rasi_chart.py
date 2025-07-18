import datetime

import pytz
import swisseph as swe

# Set Lahiri ayanamsa for sidereal zodiac
swe.set_sid_mode(swe.SIDM_LAHIRI)


def generate_rasi_chart(
    dob: str, tob: str, latitude: float, longitude: float, timezone: str = "Asia/Kolkata"
):
    """
    Generate Rasi Chart (Planetary Positions and Ascendant) using Lahiri sidereal system (as per BPHS).
    """
    # Combine date and time
    naive_dt = datetime.datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
    tz = pytz.timezone(timezone)
    local_dt = tz.localize(naive_dt)
    utc_dt = local_dt.astimezone(pytz.utc)

    # Convert to Julian Day in UT
    jd_ut = swe.julday(
        utc_dt.year,
        utc_dt.month,
        utc_dt.day,
        utc_dt.hour + utc_dt.minute / 60 + utc_dt.second / 3600,
    )

    # Planet IDs in Swiss Ephemeris
    planet_ids = {
        "Sun": swe.SUN,
        "Moon": swe.MOON,
        "Mars": swe.MARS,
        "Mercury": swe.MERCURY,
        "Jupiter": swe.JUPITER,
        "Venus": swe.VENUS,
        "Saturn": swe.SATURN,
        "Rahu": swe.MEAN_NODE,
        "Ketu": -1,  # Will derive as 180 deg opposite of Rahu
    }

    signs = [
        "Aries",
        "Taurus",
        "Gemini",
        "Cancer",
        "Leo",
        "Virgo",
        "Libra",
        "Scorpio",
        "Sagittarius",
        "Capricorn",
        "Aquarius",
        "Pisces",
    ]

    # Get planetary positions
    grahas = {}
    for name, pid in planet_ids.items():
        if name == "Ketu":
            continue  # we'll handle later
        lon = swe.calc_ut(jd_ut, pid)[0][0]
        grahas[name] = {"degree": lon % 30, "sign": signs[int(lon // 30)]}

    # Calculate Ketu
    rahu_lon = swe.calc_ut(jd_ut, swe.MEAN_NODE)[0][0]
    ketu_lon = (rahu_lon + 180) % 360
    grahas["Ketu"] = {"degree": ketu_lon % 30, "sign": signs[int(ketu_lon // 30)]}

    # Calculate Ascendant and house cusps
    houses, ascmc = swe.houses_ex(jd_ut, latitude, longitude, b"A", swe.FLG_SIDEREAL)
    asc_deg = ascmc[0]  # Ascendant degree
    asc_sign = signs[int(asc_deg // 30)]

    # Map houses to signs
    houses_dict = {}
    for i in range(12):
        deg = houses[i]
        sign = signs[int(deg // 30)]
        houses_dict[str(i + 1)] = sign

    return {
        "ascendant": asc_sign,
        "ascendant_degree": asc_deg % 30,
        "houses": houses_dict,
        "grahas": grahas,
    }
