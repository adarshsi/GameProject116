
Womb = ['Adarsh','Gutsin', 'SirHype', 'PlayerXX', 'Alpha', 'Beta', 'EchoZF']

def ActivePlayers():
    Active = []
    Count = {}
    filename = "PlayersInfo"
    with open(filename) as f:
        for line in f:
            if line.startswith("//"):
                None
            else:
                line = line.rstrip("\n")
                contents = line.split(",")
                Active.append(contents[0])
    return Active

def Filter(players, limit):
    return players[:limit]

def Winner(players):
    limit = Filter(players,1)
    return limit

print(Filter(Womb))




