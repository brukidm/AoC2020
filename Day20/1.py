import numpy as np


def check_line_up(m1, m2):
    if np.array_equal(m1[0], m2[-1]):
        return "top"
    elif np.array_equal(m1[-1], m2[0]):
        return "bot"
    elif np.array_equal([row[0] for row in m1], [row[-1] for row in m2]):
        return "left"
    elif np.array_equal([row[-1] for row in m1], [row[0] for row in m2]):
        return "right"
    else:
        return None

with open(r"input") as f:
    lines = f.read().split("\n")

    tiles = {}
    image = []

    key = ""
    for line in lines:
        if not line:
            tiles[key] = [np.array(image)]
            image = []
            continue
        if "Tile" in line:
            key = line.split(" ")[1][:-1]
        else:
            image.append(list(line))

    for key, tile in tiles.items():
        tiles[key].append(np.rot90(tile[0], 1))
        tiles[key].append(np.rot90(tile[0], 2))
        tiles[key].append(np.rot90(tile[0], 3))
        tiles[key].append(np.flip(tile[0]))
        tiles[key].append(np.rot90(np.fliplr(tile[0]), 1))
        tiles[key].append(np.rot90(np.fliplr(tile[0]), 2))
        tiles[key].append(np.rot90(np.fliplr(tile[0]), 3))


    total = {}
    for k1, tm1 in tiles.items():
        for t1 in tm1:
            count = 0
            for k2, tm2 in tiles.items():
                    if k1 != k2:
                        for t2 in tm2:
                            if check_line_up(t1, t2):
                                count += 1
            print(k1, count)

    print(dict(sorted(total.items(), key=lambda item: item[1])))



