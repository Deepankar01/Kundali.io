# Planetary natural relationship matrix from BPHS (simplified version)
natural_relationships = {
    "Sun": {
        "friends": ["Moon", "Mars", "Jupiter"],
        "enemies": ["Venus", "Saturn"],
        "neutral": ["Mercury"]
    },
    "Moon": {
        "friends": ["Sun", "Mercury"],
        "enemies": [],
        "neutral": ["Mars", "Jupiter", "Venus", "Saturn"]
    },
    "Mars": {
        "friends": ["Sun", "Moon", "Jupiter"],
        "enemies": ["Mercury"],
        "neutral": ["Venus", "Saturn"]
    },
    "Mercury": {
        "friends": ["Sun", "Venus"],
        "enemies": ["Moon"],
        "neutral": ["Mars", "Jupiter", "Saturn"]
    },
    "Jupiter": {
        "friends": ["Sun", "Moon", "Mars"],
        "enemies": ["Venus", "Mercury"],
        "neutral": ["Saturn"]
    },
    "Venus": {
        "friends": ["Mercury", "Saturn"],
        "enemies": ["Sun", "Moon"],
        "neutral": ["Mars", "Jupiter"]
    },
    "Saturn": {
        "friends": ["Mercury", "Venus"],
        "enemies": ["Sun", "Moon"],
        "neutral": ["Mars", "Jupiter"]
    }
}

# Sign ownership mapping (needed for dignity)
sign_lords = {
    "Aries": "Mars",
    "Taurus": "Venus",
    "Gemini": "Mercury",
    "Cancer": "Moon",
    "Leo": "Sun",
    "Virgo": "Mercury",
    "Libra": "Venus",
    "Scorpio": "Mars",
    "Sagittarius": "Jupiter",
    "Capricorn": "Saturn",
    "Aquarius": "Saturn",
    "Pisces": "Jupiter"
}

# Moolatrikona signs per planet (from BPHS)
moolatrikona_signs = {
    "Sun": "Leo",
    "Moon": "Taurus",
    "Mars": "Aries",
    "Mercury": "Virgo",
    "Jupiter": "Sagittarius",
    "Venus": "Libra",
    "Saturn": "Aquarius"
}

# Dignity strength values
dignity_scores = {
    "moolatrikona": 45,
    "own": 30,
    "great_friend": 20,
    "friend": 15,
    "neutral": 10,
    "enemy": 4,
    "great_enemy": 2
}

# Function to get dignity of a planet in a given sign
def get_dignity(planet: str, sign: str):
    if planet not in sign_lords.values():
        return "neutral"
    if moolatrikona_signs.get(planet) == sign:
        return "moolatrikona"
    elif sign_lords[sign] == planet:
        return "own"
    else:
        lord = sign_lords[sign]
        if planet in natural_relationships[lord]["friends"]:
            return "friend"
        elif planet in natural_relationships[lord]["enemies"]:
            return "enemy"
        elif planet in natural_relationships[lord]["neutral"]:
            return "neutral"
        else:
            return "neutral"  # fallback

# # Test dignity lookup
# test_dignities = {
#     (planet, sign): get_dignity(planet, sign)
#     for planet in moolatrikona_signs.keys()
#     for sign in sign_lords.keys()
# }

# test_dignities_list = [(k[0], k[1], v) for k, v in test_dignities.items()]
# import pandas as pd
# import ace_tools as tools
# tools.display_dataframe_to_user(name="Planetary Dignity in Signs", dataframe=pd.DataFrame(test_dignities_list, columns=["Planet", "Sign", "Dignity"]))
