from functools import reduce

with open(r"input") as f:
    lines = f.read().split("\n")
    ids = lines[1].split(",")
    buses = []
    
    for i in range(len(ids)):
        if ids[i] != "x":
            buses.append((i, ids[i]))

    timestamp = 1
    increment = 1

    adding_buses = [(buses[0][0], int(buses[0][1]))]
    for bus in buses[1:]:
        adding_buses.append((bus[0], int(bus[1])))
        while True:
            valid = True
            for nbus in adding_buses:
                if not (timestamp + nbus[0]) % nbus[1] == 0:
                    valid = False
                    break
            if valid:
                to_multiply = []
                for nbus in adding_buses:
                    to_multiply.append(nbus[1])
                increment = reduce(lambda x, y: x*y, to_multiply)
                break
            timestamp += int(increment)
    print(timestamp)


            