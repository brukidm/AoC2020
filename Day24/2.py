tiles = {}
import operator
from copy import deepcopy


def neighbors(tile):
    directions = [
                [(+1, 0), (+1, -1), (0, -1), (-1, 0), (0, +1), (+1, +1)],

        [(+1, 0), (0, -1), (-1, -1), (-1, 0), (-1, +1), (0, +1)],
    ]
    parity = tile[1] % 2
    directions = directions[parity]
    return directions


with open(r"input") as f:
    lines = f.read().split("\n")
    for line in lines:
        # e, se, sw, w, nw, and ne
        i = 0
        x = 0
        y = 0
        z = 0
        while i < len(line):
            direction = line[i]
            if direction not in ("e", "w"):
                i += 1
                direction += line[i]
            i += 1

            if direction == "e":
                x += 1
            elif direction == "w":
                x -= 1
            elif direction == "ne":
                if y % 2 == 0:
                    y -= 1
                    x += 1
                else:
                    y -= 1
            elif direction == "nw":
                if y % 2 == 0:
                    y -= 1
                else:
                    y -= 1
                    x -= 1
            elif direction == "se":
                if y % 2 == 0:
                    x += 1
                    y += 1
                else:
                    y += 1
            elif direction == "sw":
                if y % 2 == 0:
                    y += 1
                else:
                    y += 1
                    x -= 1
        if (x, y) not in tiles:
            tiles[(x, y)] = "#"
        else:
            tiles[(x, y)] = "."

    days = -1
    while days < 100:
        xs, ys = zip(*tiles.keys())
        for i in range(min(xs) - 1, max(xs) + 2):
            for j in range(min(ys) - 1, max(ys) + 2):
                coord = (i, j)
                if coord not in tiles:
                    tiles[coord] = "."
        new_tiles = deepcopy(tiles)
        for tile in tiles:
            adjs = neighbors(tile)
            black_adj = 0
            for adj in adjs:
                neigh = tuple(map(operator.add, tile, adj))
                if neigh in tiles:
                    if tiles[neigh] == "#":
                        black_adj += 1
                else:
                    new_tiles[neigh] = "."
            if tiles[tile] == "#" and (black_adj == 0 or black_adj > 2):
                new_tiles[tile] = "."
            elif tiles[tile] == "." and black_adj == 2:
                new_tiles[tile] = "#"
            else:
                new_tiles[tile] = tiles[tile]
        days += 1
        total = 0
        for c in tiles.values():
            if c == "#":
                total += 1
        print(days, total)
        tiles = new_tiles
