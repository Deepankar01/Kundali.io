import datetime
import pytz
import swisseph as swe
# Correct use of keyword arguments for rise_trans
def calculate_kala_bala(chart, dob: str, tob: str, latitude: float, longitude: float, timezone: str = "Asia/Kolkata"):
    naive_dt = datetime.datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
    tz = pytz.timezone(timezone)
    local_dt = tz.localize(naive_dt)
    utc_dt = local_dt.astimezone(pytz.utc)

    jd_ut = swe.julday(utc_dt.year, utc_dt.month, utc_dt.day,
                       utc_dt.hour + utc_dt.minute / 60 + utc_dt.second / 3600)

    geopos = (longitude, latitude, 0)  # lon, lat, elevation

    # Sunrise and sunset using correct keyword arguments
    sunrise_data = swe.rise_trans(jd_ut, swe.SUN, geopos=geopos, rsmi=swe.CALC_RISE)[1]
    sunset_data = swe.rise_trans(jd_ut, swe.SUN, geopos=geopos, rsmi=swe.CALC_SET)[1]
    sunrise_jd = sunrise_data[0]
    sunset_jd = sunset_data[0]

    is_day_chart = sunrise_jd <= jd_ut <= sunset_jd

    # Moon phase
    moon_lon = swe.calc_ut(jd_ut, swe.MOON)[0][0]
    sun_lon = swe.calc_ut(jd_ut, swe.SUN)[0][0]
    moon_phase = (moon_lon - sun_lon) % 360
    paksha = "Shukla" if moon_phase < 180 else "Krishna"

    # Nathonnatha Bala
    day_planets = ["Sun", "Jupiter", "Saturn"]
    night_planets = ["Moon", "Venus", "Mars"]
    neutral = ["Mercury"]

    nathonnatha_bala = {}
    for p in chart["grahas"]:
        if p in neutral:
            virupas = 30
        elif is_day_chart and p in day_planets:
            virupas = 60
        elif not is_day_chart and p in night_planets:
            virupas = 60
        else:
            virupas = 0
        nathonnatha_bala[p] = virupas

    # Paksha Bala
    if paksha == "Shukla":
        paksha_bala = {
            "Moon": 60, "Jupiter": 30, "Venus": 30,
            "Mars": 15, "Saturn": 15, "Sun": 30, "Mercury": 30
        }
    else:
        paksha_bala = {
            "Moon": 60, "Mars": 30, "Saturn": 30,
            "Jupiter": 15, "Venus": 15, "Sun": 30, "Mercury": 30
        }

    # Combine
    kala_bala = {}
    for p in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]:
        total = nathonnatha_bala.get(p, 0) + paksha_bala.get(p, 0)
        kala_bala[p] = {
            "Nathonnatha": nathonnatha_bala.get(p, 0),
            "Paksha": paksha_bala.get(p, 0),
            "KalaBalaVirupas": total,
            "KalaBalaRupas": round(total / 60, 2)
        }

    return kala_bala

