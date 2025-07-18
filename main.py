from generate_rasi_chart import generate_rasi_chart
from detect_yogas import detect_yogas
from vimshottari_dasha import vimshottari_dasha
from vimshottari_antardasha import vimshottari_antardasha
from navamsa_chart import calcluate_navamsa_chart
from varga_chart import calculate_varga_chart
from divisional_rules import BPHS_DIVISIONAL_RULES
from plotting.plot_north_style import draw_north_indian_chart

chart = generate_rasi_chart("1990-05-15", "14:30", 28.6139, 77.2090)
print(chart)
yogas = detect_yogas(chart)
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


fig = draw_north_indian_chart(chart)