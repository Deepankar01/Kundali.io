import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from generate_rasi_chart import generate_rasi_chart
from navamsa_chart import calcluate_navamsa_chart
from chara_karakas import get_chara_karakas
from divisional_rules import BPHS_DIVISIONAL_RULES
from varga_chart import calculate_varga_chart
from plotting.utils import prepare_planets_by_house
from vimshottari_dasha import vimshottari_dasha
from vimshottari_antardasha import vimshottari_antardasha

@pytest.fixture(scope="module")
def chart():
    return generate_rasi_chart("1990-05-15", "14:30", 28.6139, 77.2090)

def test_generate_rasi_chart_basic(chart):
    assert chart["ascendant"] == "Virgo"
    assert chart["grahas"]["Sun"]["sign"] == "Taurus"
    assert chart["grahas"]["Moon"]["sign"] == "Capricorn"
    assert chart["houses"]["1"] == "Virgo"

def test_navamsa_chart(chart):
    navamsa = calcluate_navamsa_chart(chart)
    assert navamsa["Sun"]["navamsa_sign"] == "Leo"
    assert navamsa["Ketu"]["navamsa_sign"] == "Cancer"

def test_chara_karakas(chart):
    karakas = get_chara_karakas(chart)
    expected = {
        "Atmakaraka": "Mars",
        "Amatyakaraka": "Rahu",
        "Bhratru Karaka": "Moon",
        "Matru Karaka": "Saturn",
        "Pitru Karaka": "Jupiter",
        "Putra Karaka": "Sun",
        "Gnati Karaka": "Mercury",
        "Dara Karaka": "Venus",
    }
    assert karakas == expected

def test_varga_chart_d7(chart):
    rules = BPHS_DIVISIONAL_RULES["D7"]
    d7_chart = calculate_varga_chart(chart, rules["division"], rules["rules"])
    assert d7_chart["Sun"]["sign"] == "Aries"
    assert d7_chart["Jupiter"]["sign"] == "Pisces"

def test_prepare_planets_by_house(chart):
    pb = prepare_planets_by_house(chart)
    assert len(pb) == 12
    assert pb["1"][0] == "ASC"
    assert set(pb["5"]) == {"Moon", "Saturn"}

def test_vimshottari_dasha(chart):
    sequence = vimshottari_dasha(chart)
    assert len(sequence) == 9
    first = sequence[0]
    assert first["lord"] == "Mars"
    assert pytest.approx(first["years"], rel=1e-2) == 5.8
    assert first["partial"] is True

def test_vimshottari_antardasha(chart):
    mahadasha = vimshottari_dasha(chart)
    antardasha = vimshottari_antardasha(mahadasha)
    assert len(antardasha) == 9
    first = antardasha[0]
    assert first["mahadasha_lord"] == "Mars"
    assert len(first["antardashas"]) == 9
    assert first["antardashas"][0]["lord"] == "Ketu"
