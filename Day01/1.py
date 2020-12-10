with open(r"input") as f:
    values = f.read().split('\n')
    for i in range(0, len(values)):
        for j in range(i+1, len(values)):
            if int(values[i]) + int(values[j]) == 2020:
                print(int(values[i]) * int(values[j]))