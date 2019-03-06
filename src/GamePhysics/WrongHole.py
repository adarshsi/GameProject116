
Womb = []

def ActivePlayers():
    Active = []
    filename = "PlayersInfo"
    with open(filename) as f:
        for line in f:
            if line.startswith("//"):
                None
            else:
                line = line.rstrip("\n")
                contents = line.split(",")
                Active.append(contents[0])
                Active = sorted(Active, key=str.lower)
    return Active

def Filter(username):
    index = 0
    Active = ActivePlayers()
    for names in Active:
        if username == names:
            index = Active.index(username)
    Active.pop(index)
    return Active

print(Filter("adarshsi"))



