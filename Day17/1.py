from copy import deepcopy

with open(r"input") as f:
    lines = f.read().split("\n")

    cubes = {}

    cycles = 0

    # add starting matrix to the cube
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            cubes[(0, x, y)] = lines[x][y]

    while cycles < 6:
        new_cubes = deepcopy(cubes)
        for cube in cubes:
            active_adj = 0
            for z in range(cube[0] - 1, cube[0] + 2):
                for x in range(cube[1] - 1, cube[1] + 2):
                    for y in range(cube[2] - 1, cube[2] + 2):
                        if z == cube[0] and x == cube[1] and y == cube[2]:
                            continue
                        if (z, x, y) not in cubes:
                            adj = 0
                            for z1 in range(z - 1, z + 2):
                                for x1 in range(z - 1, z + 2):
                                    for y1 in range(z - 1, z + 2):
                                        if (z1, x1, y1) in cubes:
                                            if cubes[(z1, x1, y1)] == "#":
                                                adj += 1
                            if adj == 3:
                                new_cubes[(z, x, y)] = "#"
                            else:
                                new_cubes[(z, x, y)] = "."
                        else:
                            if cubes[(z, x, y)] == "#":
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
