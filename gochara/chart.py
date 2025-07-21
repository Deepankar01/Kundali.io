import datetime
import swisseph as swe

# Step 1: Generate Gochara (Transit) chart for given date and place
def generate_gochara_chart(date: str, lat: float, lon: float):
    swe.set_sid_mode(swe.SIDM_LAHIRI)
    dt = datetime.datetime.strptime(date, "%Y-%m-%d")
    jd_ut = swe.julday(dt.year, dt.month, dt.day, 0.0)

    signs = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
             "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

    grahas = {}
    for name, pid in zip(["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"],
                         [swe.SUN, swe.MOON, swe.MARS, swe.MERCURY, swe.JUPITER, swe.VENUS, swe.SATURN]):
        lon_deg = swe.calc_ut(jd_ut, pid)[0][0]
        sign = signs[int(lon_deg // 30)]
        degree = lon_deg % 30
        grahas[name] = {"sign": sign, "degree": degree}

    return {"date": date, "grahas": grahas}
