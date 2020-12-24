coordinates = []

with open(r"input") as f:
    lines = f.read().split("\n")
    for line in lines:
        #e, se, sw, w, nw, and ne
        i = 0
        x = 0
        y = 0
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
                    y -=1
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
                if y% 2 == 0:
                    y += 1
                else:
                    y += 1
                    x -= 1
        if (x, y) not in coordinates:
            coordinates.append((x, y))
        else:
            coordinates.remove((x, y))
    print(len(coordinates))