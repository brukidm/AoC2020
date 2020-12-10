with open(r"input") as f:
    lines = f.read().split("\n")
    i = 0
    j = 25
    while i < len(lines):
        valid_numbers = lines[i:j]
        found = False
        k = i
        l = j
        for num1 in lines[k:l]:
            for num2 in lines[k:l]:
                if int(num1) + int(num2) == int(lines[j]):
                    found = True
                    l += 1
                    break
                l += 1
            if found:
                k += 1
                break
            k += 1

        if not found:
            print(lines[j])
            break
        i += 1
        j += 1