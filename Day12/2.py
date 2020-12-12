import math
axis = {
    "N": ("y", 1),
    "E": ("x", 1),
    "S": ("y", -1),
    "W": ("x", -1)
}

directions = ["N", "E", "S", "W"]

def rotate(point, instruction, angle):
    if instruction == "R":
        angle = -angle
    ox, oy = (0, 0)
    px, py = point

    qx = ox + math.cos(math.radians(angle)) * (px - ox) - math.sin(math.radians(angle)) * (py - oy)
    qy = oy + math.sin(math.radians(angle)) * (px - ox) + math.cos(math.radians(angle)) * (py - oy)
    return round(qx), round(qy)

with open(r"input") as f:
    lines = f.read().split("\n")
    direction = "E"
    x, y = 0, 0
    wp_x, wp_y = 10, 1
    position = (x,y)
    for line in lines:
        instruction, amount = line[0], int(line[1:])
        if instruction in ("L, R"):
            wp_x, wp_y = rotate((wp_x, wp_y), instruction, amount)

        if instruction == "F":
            axe, axe_sign = axis[direction]
            x += amount * wp_x * axe_sign 
            y += amount * wp_y  * axe_sign

        if instruction in axis:
            axe, axe_sign = axis[instruction]
            if axe == "x":
                wp_x += amount * axe_sign 
            else:
                wp_y += amount  * axe_sign 
    print(abs(x) + abs(y))
