axis = {
    "N": ("y", 1),
    "E": ("x", 1),
    "S": ("y", -1),
    "W": ("x", -1)
}

directions = ["N", "E", "S", "W"]

def change_direction(instruction, direction, amount):

    index = directions.index(direction)
    if amount == 90:
        amount = 1
    elif amount == 180:
        amount = 2
    else:
        amount = 3
    if instruction == "L":
        index = index - amount
    else:
        index = index + amount
    
    return directions[index % 4]



with open(r"input") as f:
    lines = f.read().split("\n")
    direction = "E"
    x, y = 0, 0
    position = (x,y)
    for line in lines:
        instruction, amount = line[0], int(line[1:])
        if instruction in ("L, R"):
            direction = change_direction(instruction, direction, amount)
            continue

        if instruction == "F":
            axe, axe_sign = axis[direction]
            if axe == "x":
                x += amount * axe_sign 
            else:
                y += amount * axe_sign

        if instruction in axis:
            axe, axe_sign = axis[instruction]
            if axe == "x":
                x += amount * axe_sign 
            else:
                y += amount * axe_sign
    print(abs(x) + abs(y))
