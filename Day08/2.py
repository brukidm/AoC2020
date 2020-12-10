import copy

with open(r"input") as f:
    lines = f.read().split("\n")
    j = 0
    while j < len(lines):
        i = 0
        accumulator = 0
        used_instructions = []
        new_list = copy.deepcopy(lines)
        op, val = lines[j].split(" ")
        if op == "jmp":
            new_list[j] = new_list[j].replace("jmp", "nop")
        elif op == "nop":
            new_list[j] = new_list[j].replace("nop", "jmp")
        while i < len(new_list):
            broken = False
            op, val = new_list[i].split(" ")
            if i in used_instructions:
                broken = True
                break
            used_instructions.append(i)

            if op == "nop":
                i += 1
            elif op == "acc":
                accumulator += int(val)
                i += 1
            else:
                i += int(val)
        j += 1
        if not broken:
            print(accumulator)
            exit