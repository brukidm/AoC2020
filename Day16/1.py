import re

valid_numbers = set()

with open(r"input") as f:
    lines = f.read().split("\n")

    i = 0

    while lines[i]:
        print(lines[i])
        numbers = re.findall(r"\d+", lines[i])
        first_range = list(range(int(numbers[0]), int(numbers[1]) + 1))
        second_range = list(range(int(numbers[2]), int(numbers[3]) + 1))
        valid_numbers.update(first_range)
        valid_numbers.update(second_range)
        i += 1

    i += 1

    while lines[i]:
        if not any(char.isdigit() for char in lines[i]):
            i += 1
            continue
        my_ticket = lines[i]
        i += 1

    i += 1

    rate = 0
    while i < len(lines):
        numbers = lines[i].split(",")
        if len(numbers) > 1:
            for number in numbers:
                if int(number) not in valid_numbers:
                    rate += int(number)
        i += 1
    print(rate)