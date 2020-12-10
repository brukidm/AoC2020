with open(r"input") as f:
    lines = f.read().split("\n")
    for i in range(len(lines)):
        if int(lines[i]) > 22406676:
            limit = i
            break

    start = 0
    end = 2
    while start < limit:
        while end < limit:
            seq = lines[start:end]
            total = sum(map(int, seq))
            if total == 22406676:
                ints = [int(i) for i in seq]
                print(max(ints) + min(ints))
                exit
            end += 1
        start += 1
        end = start + 1