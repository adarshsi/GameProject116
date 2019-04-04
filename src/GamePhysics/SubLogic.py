
Womb = ['Adarsh','Gutsin', 'SirHype', 'PlayerXX', 'Alpha', 'Beta', 'EchoZF']

import math
import random

ActiveInfo = {"Adarsh": [1,2], "Gutsin": [1,2], "SirHype": [1,1]}

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def ActivePlayers(file):
    Active = []
    compare = []
    count = {}
    filename = file
    with open(filename) as f:
        for line in f:
            if line.startswith("//"):
                None
            else:
                line = line.rstrip("\n")
                contents = line.split(", ")
                count[contents[0]] = contents[1]

    for time in count.values():
        compare.append(time)
        compare = sorted(compare)

    for items in compare:
        for name,time in count.items():
            if items == time:
                Active.append(name)

    return Active


def SpermCollector(playerlocation):
    Womb = []

    #WombPosition
    x1 = 800/200
    y1 = 600/200

    #PlayerPosition
    for keys,elements in playerlocation.items():
        if not elements:
            None
        elif type(elements[0]) is str or type(elements[1]) is str:
            None
        else:
            x2 = elements[0]
            y2 = elements[1]
            distance = math.sqrt((y2 - y1)**2 + (x2-x1)**2)
            if distance == 0:
                Womb.append(keys)
    Womb.reverse()
    return Womb


def Elimination(playerlocation, delete):
    result = []
    for names in playerlocation.keys():
        if type(names) == str or type(delete) == str:
            if names == delete:
                playerlocation.pop(names)
        else:
            del playerlocation[names]
    return playerlocation


def checkHole(playerlocation, holelocation):
    for keys,elements in playerlocation.items():
        if not elements:
            del playerlocation[keys]
        elif type(elements[0]) is str or type(elements[1]) is str:
            del playerlocation[keys]
        else:
            if elements == holelocation:
                Elimination(playerlocation, keys)
    return playerlocation


def Filter(playerlocation, limit):
    Active = []
    for names in playerlocation.keys():
        if type(names) == str and type(limit) == int:
            Active.append(names)
        else:
            None

    if limit < len(Active):
        return Active[:limit]
    else:
        return Active

def Winner():
    limit = Filter(ActiveInfo, 1)
    return limit[0]





