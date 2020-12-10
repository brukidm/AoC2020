accumulator = 0

used_instructions = []

with open(r"input") as f:
    lines = f.read().split("\n")
    i = 0
    while i < len(lines):
        op, val = lines[i].split(" ")
        if i in used_instructions:
            if op == "nop":
                lines[i].replace("nop", "jmp")
            else:
                lines[i].replace("jmp", "nop")
            break
        used_instructions.append(i)

        if op == "nop":
            i += 1
        elif op == "acc":
            accumulator += int(val)
            i += 1
        else:
            i += int(val)
    print(accumulator)