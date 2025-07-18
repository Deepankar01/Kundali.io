# Define the 7 vargas for Saptavargaja Bala with rules
from saptavargaja.relation import get_dignity, dignity_scores
from varga_chart import calculate_varga_chart


saptavarga_rules = {
    "D1": {"division": 1, "rules": {"same_as_sign": True}},
    "D2": {"division": 2, "rules": {"odd_even_based": {"odd": 0, "even": 0}}},
    "D3": {"division": 3, "rules": {"odd_even_based": {"odd": 0, "even": 0}}},
    "D7": {"division": 7, "rules": {"odd_even_based": {"odd": 0, "even": 6}}},
    "D9": {"division": 9, "rules": {"type_based": {"movable": 0, "fixed": 8, "dual": 4}}},
    "D12": {"division": 12, "rules": {"odd_even_based": {"odd": 0, "even": 0}}},
    "D30": {"division": 30, "rules": {"odd_even_based": {"odd": 0, "even": 6}}}
}

# Compute Saptavargaja Bala
def calculate_saptavargaja_bala(chart):
    dignity_table = {}
    for varga, config in saptavarga_rules.items():
        division = config["division"]
        rules = config["rules"]
        if "same_as_sign" in rules:
            varga_signs = {g: chart['grahas'][g]['sign'] for g in chart['grahas']}
        else:
            varga_signs = calculate_varga_chart(chart, division, rules)

        for graha, sign in varga_signs.items():
            if graha not in dignity_table:
                dignity_table[graha] = []
            dignity = get_dignity(graha, sign)
            dignity_table[graha].append(dignity_scores.get(dignity, 0))

    saptavarga_bala = {g: {
        "VargaStrengths": dignity_table[g],
        "TotalVirupas": sum(dignity_table[g]),
        "TotalRupas": round(sum(dignity_table[g]) / 60, 2)
    } for g in dignity_table}

    return saptavarga_bala

# Compute and display
# saptavargaja_bala = calculate_saptavargaja_bala(chart)
# tools.display_dataframe_to_user(name="Saptavargaja Bala", dataframe=pd.DataFrame(saptavargaja_bala).T)
