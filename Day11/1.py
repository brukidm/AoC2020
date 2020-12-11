from copy import deepcopy
import numpy

def get_adjacent(x, y, X, Y, matrix):
    adjacents =  lambda x, y : [(x2, y2) for x2 in range(x-1, x+2)
                               for y2 in range(y-1, y+2)
                               if (-1 < x < X and
                                   -1 < y < Y and
                                   (x != x2 or y != y2) and
                                   (0 <= x2 < X) and
                                   (0 <= y2 < Y))]
    values = []
    for adjacent in adjacents(x, y):
        values.append(matrix[adjacent[0]][adjacent[1]])
    return values

with open(r"input") as f:
    lines = f.read().split("\n")
    matrix = []
    for line in lines:
        matrix.append([x for x in line])
    while True:
        new_matrix = deepcopy(matrix)
        changed = False
        for i in range(len(matrix)): #rows
            for j in range(len(matrix[i])): #columns
                if matrix[i][j] != ".":
                    adjacents = get_adjacent(i, j, len(matrix), len(matrix[i]), matrix)
                    if matrix[i][j] == "L" and adjacents.count("#") == 0:
                        new_matrix[i][j] = "#"
                        changed = True
                    elif matrix[i][j] == "#" and adjacents.count("#") >= 4:
                        new_matrix[i][j] = "L"
                        changed = True
        if not changed:
            total = 0
            for row in new_matrix:
                total += row.count("#")
            print(total)
            exit()
        matrix = deepcopy(new_matrix)

