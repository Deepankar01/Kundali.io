# Naisargika Bala - Natural strength (fixed values from BPHS)
def calculate_naisargika_bala():
    naisargika_values = {
        "Sun": 60.0,
        "Moon": 51.43,
        "Venus": 42.86,
        "Jupiter": 34.29,
        "Mercury": 25.71,
        "Mars": 17.14,
        "Saturn": 8.57
    }

    naisargika_bala = {
        graha: {
            "NaisargikaBalaVirupas": round(v, 2),
            "NaisargikaBalaRupas": round(v / 60, 3)
        }
        for graha, v in naisargika_values.items()
    }

    return naisargika_bala
