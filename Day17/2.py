from copy import deepcopy

with open(r"input") as f:
    lines = f.read().split("\n")

    cubes = {}

    cycles = 0

    # add starting matrix to the cube
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            cubes[(x, y, 0, 0)] = lines[x][y]

    while cycles < 7:
        xs, ys, zs, ws = zip(*cubes.keys())
        for i in range(min(xs) - 1, max(xs) + 2):
            for j in range(min(ys) - 1, max(ys) + 2):
                for k in range(min(zs) - 1, max(zs) + 2):
                    for l in range(min(ws) - 1, max(ws) + 2):
                        coord = (i, j, k, l)
                        if coord not in cubes:
                            cubes[coord] = "."
        new_cubes = deepcopy(cubes)
        for cube in cubes:
            active_adj = 0
            for x in range(cube[0] - 1, cube[0] + 2):
                for y in range(cube[1] - 1, cube[1] + 2):
                    for z in range(cube[2] - 1, cube[2] + 2):
                        for w in range(cube[3] - 1, cube[3] + 2):
                            if x == cube[0] and y == cube[1] and z == cube[2] and w == cube[3]:
                                continue
                            if (x, y, z, w) not in cubes:
                                new_cubes[(x, y, z, w)] = "."
                            else:
                                if cubes[(x, y, z, w)] == "#":
                                    active_adj += 1
            if cubes[cube] == "#":
                if active_adj not in (2, 3):
                    new_cubes[cube] = "."
            elif cubes[cube] == ".":
                if active_adj == 3:
                    new_cubes[cube] = "#"
        total = 0
        for c in cubes.values():
            if c == "#":
                total += 1
        print(total)
        cubes = new_cubes
        cycles += 1
