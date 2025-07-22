import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest

from generate_rasi_chart import generate_rasi_chart
from chara_karakas import get_chara_karakas
from navamsa_chart import calcluate_navamsa_chart
from varga_chart import calculate_varga_chart
from divisional_rules import BPHS_DIVISIONAL_RULES
from divisional_charts import calculate_divisional_chart, d10_rules
from gochara.chart import generate_gochara_chart
from saptavargaja.relation import get_dignity
from saptavargaja.saptavargaja_bala import calculate_saptavargaja_bala
from shadbala.dig_bala import calculate_dig_bala
from shadbala.chesta_bala import calculate_cheshta_bala
from shadbala.kala_bala import calculate_kala_bala
from shadbala.naisargika_bala import calculate_naisargika_bala
from shadbala.drik_bala import calculate_drik_bala
from shadbala.combined import calculate_shadbala
from sthan_bala.sthan_bala import calculate_sthana_bala
from sthan_bala.sthan_bala_with_saptvarga import calculate_sthana_bala_with_saptavarga
from yoga.detect_yogas import detect_yogas
from yoga2.detect_yogas_with_auto_shadbala import detect_yogas_with_auto_shadbala


@pytest.fixture(scope="module")
def chart():
    return generate_rasi_chart("1990-05-15", "14:30", 28.6139, 77.2090)


def test_chara_karakas(chart):
    karakas = get_chara_karakas(chart)
    assert len(karakas) == 8


def test_navamsa_chart_division(chart):
    navamsa = calcluate_navamsa_chart(chart)
    assert 1 <= navamsa["Sun"]["division"] <= 9


def test_varga_chart_d10(chart):
    rules = BPHS_DIVISIONAL_RULES["D10"]
    d10 = calculate_varga_chart(chart, rules["division"], rules["rules"])
    assert "Sun" in d10


def test_divisional_chart_generic(chart):
    d10 = calculate_divisional_chart(chart, 10, d10_rules)
    assert d10["Sun"]["division"] >= 1


def test_divisional_rules_contains_d9():
    assert "D9" in BPHS_DIVISIONAL_RULES


def test_gochara_chart():
    gochara = generate_gochara_chart("2024-01-01", 28.6, 77.2)
    assert "grahas" in gochara and "Sun" in gochara["grahas"]


def test_get_dignity():
    assert get_dignity("Mars", "Aries") == "moolatrikona"


def test_saptavargaja_bala(chart):
    bala = calculate_saptavargaja_bala(chart)
    assert bala["Sun"]["TotalVirupas"] > 0


def test_dig_bala(chart):
    assert "Sun" in calculate_dig_bala(chart)


def test_chesta_bala(chart):
    cb = calculate_cheshta_bala(chart, "1990-05-16", "14:30", 28.6139, 77.2090)
    assert "Sun" in cb


def test_kala_bala(chart):
    kb = calculate_kala_bala(chart, "1990-05-15", "14:30", 28.6139, 77.2090)
    assert kb["Sun"]["KalaBalaVirupas"] >= 0


def test_naisargika_bala():
    nb = calculate_naisargika_bala()
    assert nb["Sun"]["NaisargikaBalaVirupas"] == 60.0


def test_drik_bala(chart):
    db = calculate_drik_bala(chart)
    assert "Sun" in db


def test_shadbala_combined(chart):
    sb = calculate_shadbala(chart, "1990-05-15", "14:30", 28.6139, 77.2090)
    assert "Sun" in sb


def test_sthana_bala(chart):
    sb = calculate_sthana_bala(chart)
    assert "Sun" in sb


def test_sthana_bala_with_saptavarga(chart):
    sb = calculate_sthana_bala_with_saptavarga(chart)
    assert "Sun" in sb


def test_detect_yogas(chart):
    yogas = detect_yogas(chart)
    assert isinstance(yogas, list)


def test_detect_yogas_auto_shadbala(chart):
    yogas = detect_yogas_with_auto_shadbala(chart, "1990-05-15", "14:30", 28.6139, 77.2090)
    assert isinstance(yogas, list)
