from copy import deepcopy


def get_taken(matrix, x, y):
    taken = 0

    # up
    can_see = True
    i = x - 1
    while i >= 0:
        if matrix[i][y] == "#":
            if can_see:
                taken += 1
            break
        if matrix[i][y] == "L":
            can_see = False
            break
        i -= 1

    # down
    can_see = True
    i = x + 1
    while i < len(matrix):
        if matrix[i][y] == "#":
            if can_see:
                taken += 1
            break
        if matrix[i][y] == "L":
            can_see = False
            break

        i += 1

    # left
    can_see = True
    i = y - 1
    while i >= 0:
        if matrix[x][i] == "#":
            if can_see:
                taken += 1
            break
        if matrix[x][i] == "L":
            can_see = False
            break
        i -= 1

    # right
    can_see = True
    i = y + 1
    while i < len(matrix[x]):
        if matrix[x][i] == "#":
            if can_see:
                taken += 1
            break
        if matrix[x][i] == "L":
            can_see = False
            break
        i += 1

    # up left
    can_see = True
    i = x - 1
    j = y - 1
    while i >= 0 and j >= 0:
        if matrix[i][j] == "#":
            if can_see:
                taken += 1
            break
        if matrix[i][j] == "L":
            can_see = False
            break
        i -= 1
        j -= 1

    # up right
    can_see = True
    i = x - 1
    j = y + 1
    while i >= 0 and j < len(matrix[x]):
        if matrix[i][j] == "#":
            if can_see:
                taken += 1
            break
        if matrix[i][j] == "L":
            can_see = False
            break
        i -= 1
        j += 1

    # down left
    can_see = True
    i = x + 1
    j = y - 1
    while i < len(matrix) and j >= 0:
        if matrix[i][j] == "#":
            if can_see:
                taken += 1
            break
        if matrix[i][j] == "L":
            can_see = False
            break
        i += 1
        j -= 1

    # down right
    can_see = True
    i = x + 1
    j = y + 1
    while i < len(matrix) and j < len(matrix[x]):
        if matrix[i][j] == "#":
            if can_see:
                taken += 1
            break
        if matrix[i][j] == "L":
            can_see = False
            break
        i += 1
        j += 1

    return taken


with open(r"input") as f:
    lines = f.read().split("\n")
    matrix = []
    for line in lines:
        matrix.append([x for x in line])
    while True:
        new_matrix = deepcopy(matrix)
        changed = False
        for i in range(len(matrix)):  # rows
            for j in range(len(matrix[i])):  # columns
                if matrix[i][j] != ".":
                    taken = get_taken(matrix, i, j)
                    if matrix[i][j] == "L" and taken == 0:
                        new_matrix[i][j] = "#"
                        changed = True
                    elif matrix[i][j] == "#" and taken >= 5:
                        new_matrix[i][j] = "L"
                        changed = True
        if not changed:
            total = 0
            for row in new_matrix:
                total += row.count("#")
            print(total)
            exit()
        matrix = deepcopy(new_matrix)
