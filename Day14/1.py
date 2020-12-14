with open(r"input") as f:
    lines = f.read().split("\n")
    memory = {}
    active_mask = lines[0].split(" ")[-1].strip()

    for line in lines[1:]:
        value = line.split(" ")[-1].strip()
        if "mask" in line:
            active_mask = value
            continue
        if "mem" in line:
            write = int(value)
            write = format(write, "36b").replace(" ", "0")
            mem_loc = int(line[line.find("[") + 1 : line.find("]")])

            result = ""
            for i in range(len(active_mask)):
                if active_mask[i] == "X":
                    result += write[i]
                else:
                    result += active_mask[i]
            memory[mem_loc] = result

    sum = 0
    for val in memory.values():
        sum += int(val, 2)
    print(sum)