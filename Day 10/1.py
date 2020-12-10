with open(r"input") as f:
    lines = [int(x) for x in f.read().split("\n")]
    lines.sort()
    lines.append(lines[-1] + 3)
    one_jolts = three_jolts = 0

    current = 0
    for jolt in lines:
        print(current)
        if jolt - current == 1:
            one_jolts += 1
            current = jolt
        if jolt - current == 2:
            current = jolt
        if jolt - current == 3:
            three_jolts += 1
            current = jolt

    print(one_jolts * three_jolts)