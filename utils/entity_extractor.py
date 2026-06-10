TEAMS = [
    "MI",
    "CSK",
    "RCB",
    "KKR",
    "SRH",
    "RR",
    "DC",
    "GT",
    "LSG",
    "PBKS"
]

PLAYERS = [
    "Virat Kohli",
    "Rohit Sharma",
    "Jasprit Bumrah",
    "KL Rahul",
    "Travis Head",
    "Ruturaj Gaikwad",
    "Sanju Samson"
]


def extract_entities(query):

    entities = []

    for team in TEAMS:
        if team.lower() in query.lower():
            entities.append(team)

    for player in PLAYERS:
        if player.lower() in query.lower():
            entities.append(player)

    return entities