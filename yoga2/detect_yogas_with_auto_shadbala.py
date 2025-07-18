from shadbala.combined import calculate_shadbala
from yoga2.chakra import detect_chakra_yoga
from yoga2.chamra import detect_chamara_yoga
from yoga2.daama import detect_daama_yoga
from yoga2.duradhara import detect_duradhara_yoga
from yoga2.gada import detect_gada_yoga
from yoga2.gajakesari import detect_gajakesari_yoga
from yoga2.musala import detect_musala_yoga
from yoga2.nala import detect_nala_yoga
from yoga2.rajju import detect_rajju_yoga
from yoga2.sakta import detect_sakata_yoga
from yoga2.sunapha_anapha import detect_sunapha_anapha_yoga
from yoga2.vajra import detect_vajra_yoga
from yoga2.yava import detect_yava_yoga


def get_sign_occupancy(chart):
    signs_order = [
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
    sign_occupancy = {sign: [] for sign in signs_order}
    for graha, data in chart["grahas"].items():
        sign_occupancy[data["sign"]].append(graha)
    return sign_occupancy, signs_order


def _run_extended_yoga_detections(chart, shadbala_data):
    sign_occupancy, signs_order = get_sign_occupancy(chart)
    results = []
    detectors = [
        lambda c, s: detect_daama_yoga(c, s),
        lambda c, s: detect_duradhara_yoga(c, s, sign_occupancy, signs_order),
        lambda c, s: detect_sunapha_anapha_yoga(c, s, sign_occupancy, signs_order),
        lambda c, s: detect_gajakesari_yoga(c, s, signs_order),
        lambda c, s: detect_vajra_yoga(c, s, sign_occupancy, signs_order),
        lambda c, s: detect_yava_yoga(c, s, sign_occupancy, signs_order),
        lambda c, s: detect_sakata_yoga(c, s, signs_order),
        lambda c, s: detect_chamara_yoga(c, s, signs_order),
        lambda c, s: detect_rajju_yoga(c, s),
        lambda c, s: detect_musala_yoga(c, s),
        lambda c, s: detect_nala_yoga(c, s),
        lambda c, s: detect_chakra_yoga(c, s, sign_occupancy, signs_order),
        lambda c, s: detect_gada_yoga(c, s, sign_occupancy),
    ]
    for fn in detectors:
        result = fn(chart, shadbala_data)
        if result:
            if isinstance(result, list):
                results.extend(result)
            else:
                results.append(result)
    return results


def detect_yogas_with_auto_shadbala(
    chart: dict, dob: str, tob: str, latitude: float, longitude: float
):
    """
    Convenience wrapper to auto-calculate Shadbala and detect yogas.
    Returns full yoga list with shadbala_status and validity.
    """
    raw_shadbala = calculate_shadbala(chart, dob, tob, latitude, longitude)
    shadbala_data = {graha: int(details["TotalVirupas"]) for graha, details in raw_shadbala.items()}
    return _run_extended_yoga_detections(chart, shadbala_data)
