BPHS_DIVISIONAL_RULES = {
    "D1": {
        "name": "Rasi",
        "division": 1,
        "rules": {"same_as_sign": True}
    },
    "D2": {
        "name": "Hora",
        "division": 2,
        "rules": {
            "odd_even_based": {"odd": 0, "even": 0}  # Special treatment needed for Moon/Sun Hora
        }
    },
    "D3": {
        "name": "Drekkana",
        "division": 3,
        "rules": {
            "odd_even_based": {"odd": 0, "even": 0}  # BPHS: Each 10° goes to sign of same element
        }
    },
    "D4": {
        "name": "Chaturthamsa",
        "division": 4,
        "rules": {"same_as_sign": True}
    },
    "D5": {
        "name": "Panchamsa",
        "division": 5,
        "rules": {"same_as_sign": True}
    },
    "D6": {
        "name": "Shashtamsa",
        "division": 6,
        "rules": {"same_as_sign": True}
    },
    "D7": {
        "name": "Saptamsa",
        "division": 7,
        "rules": {
            "odd_even_based": {"odd": 0, "even": 6}
        }
    },
    "D8": {
        "name": "Ashtamsa",
        "division": 8,
        "rules": {"same_as_sign": True}
    },
    "D9": {
        "name": "Navamsa",
        "division": 9,
        "rules": {
            "type_based": {
                "movable": 0,
                "fixed": 8,
                "dual": 4
            }
        }
    },
    "D10": {
        "name": "Dasamsa",
        "division": 10,
        "rules": {
            "type_based": {
                "movable": 0,
                "fixed": 8,
                "dual": 4
            }
        }
    },
    "D11": {
        "name": "Rudramsa",
        "division": 11,
        "rules": {"same_as_sign": True}
    },
    "D12": {
        "name": "Dvadasamsa",
        "division": 12,
        "rules": {
            "odd_even_based": {"odd": 0, "even": 0}
        }
    },
    "D16": {
        "name": "Shodasamsa",
        "division": 16,
        "rules": {
            "type_based": {
                "movable": 0,
                "fixed": 8,
                "dual": 4
            }
        }
    },
    "D20": {
        "name": "Vimsamsa",
        "division": 20,
        "rules": {
            "type_based": {
                "movable": 0,
                "fixed": 8,
                "dual": 4
            }
        }
    },
    "D24": {
        "name": "Siddhamsa",
        "division": 24,
        "rules": {"same_as_sign": True}
    },
    "D27": {
        "name": "Bhamsa/Nakshatramsa",
        "division": 27,
        "rules": {
            "odd_even_based": {"odd": 0, "even": 6}
        }
    },
    "D30": {
        "name": "Trimsamsa",
        "division": 30,
        "rules": {
            "odd_even_based": {"odd": 0, "even": 6}
        }
    },
    "D40": {
        "name": "Akshavedamsa",
        "division": 40,
        "rules": {"same_as_sign": True}
    },
    "D45": {
        "name": "Khavedamsa",
        "division": 45,
        "rules": {"same_as_sign": True}
    },
    "D60": {
        "name": "Shastiamsa",
        "division": 60,
        "rules": {"same_as_sign": True}
    }
}
