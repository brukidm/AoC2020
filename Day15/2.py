mentions = {}

with open(r"input") as f:
    lines = f.read().split("\n")
    n = 1

    starting_numbers = lines[0].split(",")
    starting_numbers = [int(x) for x in starting_numbers]
    for number in starting_numbers:
        mentions[number] = [n]
        n += 1
        last_spoken = number
        added_prev = True

    while True:
        if n > 30000000:
            break
        if added_prev:
            last_spoken = 0
            if last_spoken not in mentions:
                mentions[last_spoken] = [n]
            else:
                mentions[last_spoken] = [mentions[last_spoken][-1], n]
                added_prev = False
            n += 1
        else:
            last_spoken = mentions[last_spoken][-1] - mentions[last_spoken][-2]
            if last_spoken in mentions:
                mentions[last_spoken] = [mentions[last_spoken][-1], n]
                added_prev = False
            else:
                mentions[last_spoken] = [n]
                added_prev = True
            n += 1
    print(last_spoken)