with open(r"input") as f:
    lines = f.read().split('\n')
    valid = 0
    for line in lines:
        splits = line.split(" ")
        minmax = splits[0].split("-")
        minimum = int(minmax[0])
        maximum = int(minmax[1])
        match = splits[1][0]
        count = 0
        for char in splits[-1]:
            if char == match:
                count += 1
        if minimum <= count <= maximum:
            valid +=1
print(valid)
