import math 
with open(r"input") as f:
    lines = f.read().split("\n")
    earliest = int(lines[0])
    ids = lines[1].replace("x,", "").split(",")
    ids = [int(i) for i in ids]
    departures = []
    for id in ids:
        departures.append((math.ceil(earliest / id)) * id)
    lowest = min(departures)
    bus = ids[departures.index(lowest)]
    print((lowest - earliest) * bus)