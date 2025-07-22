import types

import pytest

from divisional_charts import calculate_divisional_chart
from varga_chart import calculate_varga_chart
from saptavargaja.relation import get_dignity, natural_relationships
from shadbala.decorator import validate_shadbala
from shadbala.dig_bala import calculate_dig_bala
from shadbala.chesta_bala import calculate_cheshta_bala
from shadbala.kala_bala import calculate_kala_bala
from shadbala.combined import categorize_shadbala_strength
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
from yoga2.detect_yogas_with_auto_shadbala import _run_extended_yoga_detections

SIGNS = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]


# Helper to build empty sign occupancy
def empty_occupancy():
    return {s: [] for s in SIGNS}


def test_divisional_and_varga_default_offset():
    chart = {"grahas": {"Sun": {"sign": "Aries", "degree": 15}}}
    div = calculate_divisional_chart(chart, 9, {})
    varga = calculate_varga_chart(chart, 9, {})
    assert div["Sun"]["sign"] == "Leo"
    assert varga["Sun"]["sign"] == "Leo"


def test_get_dignity_fallback(monkeypatch):
    nr_backup = natural_relationships["Mars"].copy()
    monkeypatch.setitem(natural_relationships, "Mars", {"friends": [], "enemies": [], "neutral": []})
    try:
        assert get_dignity("Saturn", "Aries") == "neutral"
    finally:
        natural_relationships["Mars"] = nr_backup


def test_validate_shadbala_list(monkeypatch):
    @validate_shadbala(threshold=10)
    def _fn(chart):
        return [{"planets": ["Sun", "Moon"]}, {"planets": ["Mars"]}]

    result = _fn({}, {"Sun": 20, "Moon": 5, "Mars": 15})
    assert result[0]["shadbala_status"]["Sun"] == 20
    assert not result[0]["valid"]
    assert result[1]["valid"]


def test_dig_bala_missing_sign():
    chart = {
        "houses": {},
        "grahas": {g: {"sign": "Aries"} for g in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]}
    }
    res = calculate_dig_bala(chart)
    assert all(v["DigBalaVirupas"] == 0 for v in res.values())


def test_cheshta_bala_low_speed(monkeypatch):
    import swisseph as swe

    def fake_calc_ut(jd, pid):
        return ([0],)

    monkeypatch.setattr(swe, "calc_ut", fake_calc_ut)
    chart = {"grahas": {g: {} for g in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]}}
    cb = calculate_cheshta_bala(chart, "2000-01-01", "00:00", 0, 0)
    assert all(v["CheshtaBalaVirupas"] == 60 for v in cb.values())


def test_kala_bala_day_shukla(monkeypatch):
    import swisseph as swe

    def fake_rise_trans(jd, body, geopos, rsmi):
        if rsmi == swe.CALC_RISE:
            return None, (jd - 0.1,)
        return None, (jd + 0.1,)

    def fake_calc_ut(jd, body):
        return ([0],)

    monkeypatch.setattr(swe, "rise_trans", fake_rise_trans)
    monkeypatch.setattr(swe, "calc_ut", fake_calc_ut)

    chart = {"grahas": {g: {} for g in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]}}
    kb = calculate_kala_bala(chart, "2000-01-01", "00:00", 0, 0)
    assert kb["Sun"]["KalaBalaVirupas"] >= 60
    assert kb["Moon"]["Paksha"] == 60


def test_categorize_shadbala_strength():
    data = {
        "Sun": {"TotalRupas": 7.5},
        "Moon": {"TotalRupas": 3.5},
        "Mars": {"TotalRupas": 0.5},
    }
    res = categorize_shadbala_strength(data)
    assert res["Sun"]["StrengthCategory"].startswith("Very Strong")
    assert res["Moon"]["StrengthCategory"].startswith("Moderate")
    assert res["Mars"]["StrengthCategory"].startswith("Very Weak")


def test_detect_chakra_yoga():
    chart = {"ascendant": "Aries"}
    occ = empty_occupancy()
    occ["Aries"] = ["Sun"]
    occ["Cancer"] = ["Moon"]
    occ["Libra"] = ["Mars"]
    occ["Capricorn"] = ["Mercury"]
    res = detect_chakra_yoga(chart, {}, occ, SIGNS)
    assert res["yoga_name"] == "Chakra Yoga"
    assert set(res["planets"]) == {"Sun", "Moon", "Mars", "Mercury"}
    assert res["valid"] is False


def test_detect_chamara_yoga():
    chart = {
        "ascendant": "Gemini",
        "grahas": {
            "Jupiter": {"sign": "Pisces"},
            "Mercury": {"sign": "Virgo"},
        },
    }
    res = detect_chamara_yoga(chart, {p: 7000 for p in ["Jupiter", "Mercury"]}, SIGNS)
    assert len(res) == 2


def test_daama_yoga():
    chart = {"grahas": {
        "Sun": {"sign": "Aries"},
        "Moon": {"sign": "Taurus"},
        "Mars": {"sign": "Gemini"},
        "Mercury": {"sign": "Cancer"},
        "Jupiter": {"sign": "Leo"},
        "Venus": {"sign": "Virgo"},
        "Saturn": {"sign": "Virgo"},
    }}
    res = detect_daama_yoga(chart, {p: 7000 for p in chart["grahas"]})
    assert res["yoga_name"] == "Daama Yoga"


def test_other_small_yogas():
    chart = {
        "ascendant": "Aries",
        "grahas": {
            "Jupiter": {"sign": "Taurus"},
            "Moon": {"sign": "Libra"},
            "Mercury": {"sign": "Taurus"},
            "Venus": {"sign": "Taurus"},
            "Mars": {"sign": "Capricorn"},
            "Saturn": {"sign": "Capricorn"},
            "Sun": {"sign": "Cancer"},
        },
    }
    occ = empty_occupancy()
    occ["Aries"].append("Jupiter")
    occ["Capricorn"].extend(["Mars", "Saturn"])
    occ["Taurus"].extend(["Mercury", "Venus"])
    res1 = detect_duradhara_yoga(chart, {p:7000 for p in chart["grahas"]}, occ, SIGNS)
    assert res1 is None
    res2 = detect_gada_yoga(chart, {p:7000 for p in chart["grahas"]}, occ)
    assert res2 is None
    res3 = detect_gajakesari_yoga(chart, {p:7000 for p in chart["grahas"]}, SIGNS)
    assert res3 is None
    res4 = detect_musala_yoga(chart, {p:7000 for p in chart["grahas"]})
    assert res4 is None
    res5 = detect_nala_yoga(chart, {p:7000 for p in chart["grahas"]})
    assert res5 is None
    res6 = detect_rajju_yoga(chart, {p:7000 for p in chart["grahas"]})
    assert res6 is None
    res7 = detect_sakata_yoga(chart, {p:7000 for p in chart["grahas"]}, SIGNS)
    assert res7 is None
    res8 = detect_sunapha_anapha_yoga(chart, {p:7000 for p in chart["grahas"]}, occ, SIGNS)
    assert res8 is None
    occ["Aries"].append("Mercury")
    occ["Libra"].append("Venus")
    res9 = detect_vajra_yoga(chart, {p:7000 for p in chart["grahas"]}, occ, SIGNS)
    assert res9 is None
    res10 = detect_yava_yoga(chart, {p:7000 for p in chart["grahas"]}, occ, SIGNS)
    assert res10 is None


def test_run_extended_yoga_detections_list(monkeypatch):
    chart = {"grahas": {}}
    shadbala = {}
    def fake_detector(c, s):
        return [{"yoga_name": "Test", "planets": []}]
    monkeypatch.setattr('yoga2.detect_yogas_with_auto_shadbala.detect_daama_yoga', fake_detector)
    monkeypatch.setattr('yoga2.detect_yogas_with_auto_shadbala.detect_duradhara_yoga', lambda c,s,a,b: None)
    monkeypatch.setattr('yoga2.detect_yogas_with_auto_shadbala.detect_sunapha_anapha_yoga', lambda c,s,a,b: None)
    monkeypatch.setattr('yoga2.detect_yogas_with_auto_shadbala.detect_gajakesari_yoga', lambda c,s,a: None)
    monkeypatch.setattr('yoga2.detect_yogas_with_auto_shadbala.detect_vajra_yoga', lambda c,s,a,b: None)
    monkeypatch.setattr('yoga2.detect_yogas_with_auto_shadbala.detect_yava_yoga', lambda c,s,a,b: None)
    monkeypatch.setattr('yoga2.detect_yogas_with_auto_shadbala.detect_sakata_yoga', lambda c,s,a: None)
    monkeypatch.setattr('yoga2.detect_yogas_with_auto_shadbala.detect_chamara_yoga', lambda c,s,a: None)
    monkeypatch.setattr('yoga2.detect_yogas_with_auto_shadbala.detect_rajju_yoga', lambda c,s: None)
    monkeypatch.setattr('yoga2.detect_yogas_with_auto_shadbala.detect_musala_yoga', lambda c,s: None)
    monkeypatch.setattr('yoga2.detect_yogas_with_auto_shadbala.detect_nala_yoga', lambda c,s: None)
    monkeypatch.setattr('yoga2.detect_yogas_with_auto_shadbala.detect_chakra_yoga', lambda c,s,a,b: None)
    monkeypatch.setattr('yoga2.detect_yogas_with_auto_shadbala.detect_gada_yoga', lambda c,s,a: None)
    res = _run_extended_yoga_detections(chart, shadbala)
    assert res[0]["yoga_name"] == "Test"

def test_positive_small_yogas():
    # Musala Yoga - all non luminaries in fixed signs
    fixed_chart = {
        "grahas": {g: {"sign": "Taurus"} for g in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]},
        "ascendant": "Aries",
    }
    shad = {p: 7000 for p in fixed_chart["grahas"]}
    assert detect_musala_yoga(fixed_chart, shad)

    # Nala and Rajju Yogas - all in dual or movable signs
    dual_chart = {
        "grahas": {g: {"sign": "Gemini"} for g in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]},
        "ascendant": "Aries",
    }
    shad2 = {p: 7000 for p in dual_chart["grahas"]}
    assert detect_nala_yoga(dual_chart, shad2)
    movable_chart = {
        "grahas": {g: {"sign": "Aries"} for g in ["Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus", "Saturn"]},
        "ascendant": "Aries",
    }
    shad3 = {p: 7000 for p in movable_chart["grahas"]}
    assert detect_rajju_yoga(movable_chart, shad3)

    occ = empty_occupancy()
    occ["Aries"].append("Mercury")
    occ["Cancer"].append("Mars")
    occ["Libra"].append("Venus")
    occ["Capricorn"].append("Saturn")
    vajra = detect_vajra_yoga(fixed_chart, shad, occ, SIGNS)
    assert vajra and vajra["yoga_name"] == "Vajra Yoga"
    yava = detect_yava_yoga(fixed_chart, shad, occ, SIGNS)
    assert yava and yava["yoga_name"] == "Yava Yoga"

    occ2 = empty_occupancy()
    occ2["Gemini"].append("Mercury")
    occ2["Leo"].append("Moon")
    result = detect_sunapha_anapha_yoga(fixed_chart, shad, occ2, SIGNS)
    assert result and result["yoga_name"] == "Sunapha/Anapha Yoga"
