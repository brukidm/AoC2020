with open(r"input") as f:
    lines = f.read().split('\n')
    valid = 0
    for line in lines:
        splits = line.split(" ")
        positions = splits[0].split("-")
        first_pos = int(positions[0]) - 1
        second_pos = int(positions[1]) - 1
        match = splits[1][0]
        count = 0
        if match == splits[-1][first_pos] and match != splits[-1][second_pos] or match != splits[-1][first_pos] and match == splits[-1][second_pos]:
            valid +=1
print(valid)
