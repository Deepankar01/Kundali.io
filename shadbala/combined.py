# Combine all components into final Shadbala function
from shadbala.chesta_bala import calculate_cheshta_bala
from shadbala.dig_bala import calculate_dig_bala
from shadbala.drik_bala import calculate_drik_bala
from shadbala.kala_bala import calculate_kala_bala
from shadbala.naisargika_bala import calculate_naisargika_bala
from sthan_bala.sthan_bala_with_saptvarga import calculate_sthana_bala_with_saptavarga


def calculate_shadbala(chart, dob, tob, latitude, longitude, timezone="Asia/Kolkata"):
    # Gather all components
    sthana = calculate_sthana_bala_with_saptavarga(chart)
    dig = calculate_dig_bala(chart)
    kala = calculate_kala_bala(chart, dob, tob, latitude, longitude, timezone)
    cheshta = calculate_cheshta_bala(chart, dob, tob, latitude, longitude, timezone)
    naisargika = calculate_naisargika_bala()
    drik = calculate_drik_bala(chart)

    all_planets = ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]
    shadbala_summary = {}

    for p in all_planets:
        total_virupas = (
            sthana[p]["TotalVirupas"] +
            dig[p]["DigBalaVirupas"] +
            kala[p]["KalaBalaVirupas"] +
            cheshta[p]["CheshtaBalaVirupas"] +
            naisargika[p]["NaisargikaBalaVirupas"] +
            drik[p]["DrikBalaVirupas"]
        )
        shadbala_summary[p] = {
            "Sthana": sthana[p]["TotalRupas"],
            "Dig": dig[p]["DigBalaRupas"],
            "Kala": kala[p]["KalaBalaRupas"],
            "Cheshta": cheshta[p]["CheshtaBalaRupas"],
            "Naisargika": naisargika[p]["NaisargikaBalaRupas"],
            "Drik": drik[p]["DrikBalaRupas"],
            "TotalVirupas": round(total_virupas, 2),
            "TotalRupas": round(total_virupas / 60, 2)
        }

    return shadbala_summary


# Categorization function based on Shadbala Total Rupas
def categorize_shadbala_strength(shadbala_data: dict):
    thresholds = [
        (7.0, "Very Strong 🌟"),
        (5.0, "Strong 💪"),
        (3.0, "Moderate ⚖️"),
        (1.5, "Weak ⚠️"),
        (0.0, "Very Weak ❌")
    ]

    categorized = {}
    for planet, data in shadbala_data.items():
        rupas = data["TotalRupas"]
        category = next(label for value, label in thresholds if rupas >= value)
        categorized[planet] = {
            **data,
            "StrengthCategory": category
        }

    return categorized

