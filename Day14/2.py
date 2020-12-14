with open(r"input") as f:
    lines = f.read().split("\n")
    memory = {}
    active_mask = lines[0].split(" ")[-1].strip()

    for line in lines[1:]:
        value = line.split(" ")[-1].strip()
        if "mask" in line:
            active_mask = value
            continue

        write = int(value)
        mem_loc = int(line[line.find("[") + 1 : line.find("]")])
        mem_loc = format(mem_loc, "36b").replace(" ", "0")

        result = ""
        for i in range(len(active_mask)):
            if active_mask[i] == "0":
                result += mem_loc[i]
            else:
                result += active_mask[i]

        addresses = []
        for char in result:
            if not addresses:
                if char == "X":
                    addresses.append("0")
                    addresses.append("1")
                else:
                    addresses.append(char)
                continue

            new_addresses = []
            for address in addresses:
                if char != "X":
                    new_addresses.append(address + char)
                else:
                    new_addresses.append(address + "0")
                    new_addresses.append(address + "1")
            addresses = new_addresses

        for address in addresses:
            memory[address] = write

    sum = 0
    for val in memory.values():
        sum += val
    print(sum)