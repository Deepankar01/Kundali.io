# Re-imports and setup after code reset
import swisseph as swe
import datetime
import pytz


# Cheshta Bala
def calculate_cheshta_bala(
    chart, dob: str, tob: str, latitude: float, longitude: float, timezone: str = "Asia/Kolkata"
):
    naive_dt = datetime.datetime.strptime(f"{dob} {tob}", "%Y-%m-%d %H:%M")
    tz = pytz.timezone(timezone)
    local_dt = tz.localize(naive_dt)
    utc_dt = local_dt.astimezone(pytz.utc)

    jd_ut_today = swe.julday(
        utc_dt.year,
        utc_dt.month,
        utc_dt.day,
        utc_dt.hour + utc_dt.minute / 60 + utc_dt.second / 3600,
    )
    jd_ut_next = jd_ut_today + 1.0

    cheshta_bala = {}
    for planet, pid in zip(
        ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"],
        [swe.SUN, swe.MOON, swe.MARS, swe.MERCURY, swe.JUPITER, swe.VENUS, swe.SATURN],
    ):
        lon_today = swe.calc_ut(jd_ut_today, pid)[0][0]
        lon_next = swe.calc_ut(jd_ut_next, pid)[0][0]

        delta = (lon_next - lon_today + 360) % 360
        speed = delta

        if speed > 1.5:
            virupas = 7.5
        elif speed > 1.0:
            virupas = 15
        elif speed > 0.5:
            virupas = 30
        elif speed > 0.01:
            virupas = 45
        else:
            virupas = 60

        cheshta_bala[planet] = {
            "Speed(deg/day)": round(speed, 3),
            "CheshtaBalaVirupas": virupas,
            "CheshtaBalaRupas": round(virupas / 60, 2),
        }

    return cheshta_bala
