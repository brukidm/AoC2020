with open(r"input") as f:
    lines = f.read().split('\n')
    skips_right = [1, 3, 5, 7, 1]
    steps = [1, 1, 1, 1, 2]
    for i in range(0, len(skips_right)):
        trees = 0
        counter = 0
        for j in range(0, len(lines), steps[i]):
            if lines[j][counter] == "#":
                trees += 1
            counter += skips_right[i]
            counter = counter % len(lines[j])
        print(trees)