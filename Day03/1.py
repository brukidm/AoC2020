with open(r"input") as f:
    lines = f.read().split('\n')
    trees = 0
    counter = 0
    for line in lines:
        if line[counter] == "#":
            trees += 1
        counter += 3
        counter = counter % len(line)
print(trees)
