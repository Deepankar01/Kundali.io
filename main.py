from bhav.combined import interpret_all_bhavas
from bhav.summary import generate_bhava_summary
from chara_karakas import get_chara_karakas
from generate_rasi_chart import generate_rasi_chart
from yoga.detect_yogas import detect_yogas
from saptavargaja.saptavargaja_bala import calculate_saptavargaja_bala
from shadbala.chesta_bala import calculate_cheshta_bala

from shadbala.combined import calculate_shadbala, categorize_shadbala_strength
from shadbala.dig_bala import calculate_dig_bala
from shadbala.drik_bala import calculate_drik_bala
from shadbala.kala_bala import calculate_kala_bala
from shadbala.naisargika_bala import calculate_naisargika_bala
from sthan_bala.sthan_bala import calculate_sthana_bala
from sthan_bala.sthan_bala_with_saptvarga import calculate_sthana_bala_with_saptavarga
from vimshottari_dasha import vimshottari_dasha
from vimshottari_antardasha import vimshottari_antardasha
from navamsa_chart import calcluate_navamsa_chart
from varga_chart import calculate_varga_chart
from divisional_rules import BPHS_DIVISIONAL_RULES
from plotting.plot_north_style import draw_north_indian_chart
from yoga2.detect_yogas_with_auto_shadbala import detect_yogas_with_auto_shadbala

DOB = "1990-05-15"
TOB = "14:30"
LAT = 28.6139
LONG = 77.2090

chart = generate_rasi_chart(DOB, TOB, LAT, LONG)
print(chart)
yogas = detect_yogas(chart)
print("-----------")
print(yogas)
vim_dasha = vimshottari_dasha(chart)
print(vim_dasha)
antardashas = vimshottari_antardasha(vim_dasha)
print(antardashas)
navamsa = calcluate_navamsa_chart(chart)
print(navamsa)

d10_rules = BPHS_DIVISIONAL_RULES["D10"]
d10_chart = calculate_varga_chart(chart, d10_rules["division"], d10_rules["rules"])
print(d10_chart)
d7_rules = BPHS_DIVISIONAL_RULES["D7"]
d7_chart = calculate_varga_chart(chart, d7_rules["division"], d7_rules["rules"])
print(d7_chart)

chara_karakas = get_chara_karakas(chart)
print(chara_karakas)

sthana_bala = calculate_sthana_bala(chart)
print(sthana_bala)

saptavargaja_bala = calculate_saptavargaja_bala(chart)
print(saptavargaja_bala)

sthan_bala_with_saptavargaja_bala = calculate_sthana_bala_with_saptavarga(chart)
print(sthan_bala_with_saptavargaja_bala)

dig_bala = calculate_dig_bala(chart)
print(dig_bala)
kala_bala = calculate_kala_bala(chart, DOB, TOB, LAT, LONG)
print(kala_bala)
cheshta_bala = calculate_cheshta_bala(chart, DOB, TOB, LAT, LONG)
print(cheshta_bala)
naisargika_bala = calculate_naisargika_bala()
print(naisargika_bala)
drik_bala = calculate_drik_bala(chart)
print(drik_bala)

shadbala = calculate_shadbala(chart, DOB, TOB, LAT, LONG)
print(shadbala)
categorized_shadbala = categorize_shadbala_strength(shadbala)
print(categorized_shadbala)

# Run it on current chart and Shadbala
# shadbala_from_production = {graha: int(v['TotalVirupas']) for graha, v in shadbala.items()}
decorated_yoga_results = detect_yogas_with_auto_shadbala(chart, DOB, TOB, LAT, LONG)
print(decorated_yoga_results)

bhava_summary = generate_bhava_summary(chart)
print(bhava_summary)

result = interpret_all_bhavas(chart, categorized_shadbala)
print(result)
fig = draw_north_indian_chart(chart)
