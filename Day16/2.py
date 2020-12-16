import re

fields = {}
valid_values = set()

with open(r"input") as f:
    lines = f.read().split("\n")

    i = 0

    # read number ranges from input
    while lines[i]:
        numbers = re.findall(r"\d+", lines[i])
        first_range = list(range(int(numbers[0]), int(numbers[1]) + 1))
        second_range = list(range(int(numbers[2]), int(numbers[3]) + 1))

        valid_values.update(first_range + second_range)

        # add rules to the dictionary
        fields[i] = first_range + second_range
        i += 1

    i += 2

    # read my ticket
    while lines[i]:
        my_ticket = [int(x) for x in lines[i].split(",")]
        i += 1

    i += 1

    valid_tickets = [my_ticket]

    # based on the part 1, get rid of invalid tickets
    while i < len(lines):
        numbers = lines[i].split(",")
        if len(numbers) > 1:
            valid = True
            for j in range(0, len(numbers)):
                if int(numbers[j]) not in valid_values:
                    valid = False
            if valid:
                valid_tickets.append([int(x) for x in numbers])
        i += 1

    possibilities = {}

    for column in range(0, 20):
        values_in_column = set()

        # read values from each column
        for i in range(0, len(valid_tickets)):
            ticket = valid_tickets[i]
            values_in_column.add(ticket[column])

        poss = []
        # go through all the rules
        for key, values in fields.items():
            # if the column values are a subset of rules, there's a possibility
            # the column corresponds to that rule
            if values_in_column.issubset(set(fields[key])):
                poss.append(key)
        # ticket column value can respond to which positions in rules?
        possibilities[column] = poss

    positions_taken = list()
    result = 1
    # sort columns by amount of possibilities, ascending
    for k in sorted(possibilities, key=lambda k: len(possibilities[k])):
        # there will always be one possible value that's not taken
        # position is 0-5, which is first 6 rules (departure)
        position = (set(possibilities[k]) - set(positions_taken)).pop()
        positions_taken.append(position)
        if position in range(6):
            # k is index/column of a value from my_ticket
            result *= int(my_ticket[k])
    print(result)