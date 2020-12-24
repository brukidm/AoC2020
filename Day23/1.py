from itertools import cycle

with open(r"input") as f:
    lines = f.read().split("\n")
    numbers = [int(x) for x in lines[0]]

    i = 0
    counter = 1
    lowest = min(numbers)
    highest = max(numbers)

    while counter <= 100:
        print(f"-- move {counter} --")
        print("cups: ", numbers)
        current_number = numbers[i]
        destination_cup = numbers[i] - 1

        if destination_cup == 0:
            destination_cup = highest

        t, s, f = (
            numbers[(i + 3) % len(numbers)],
            numbers[(i + 2) % len(numbers)],
            numbers[(i + 1) % len(numbers)],
        )

        numbers.remove(t)
        numbers.remove(s)
        numbers.remove(f)

        print("pick up: ", f, s, t)

        if destination_cup not in (f, s, t):
            for number in numbers:
                if number == destination_cup:
                    index = numbers.index(number)
                    break
        else:
            while destination_cup not in numbers:
                destination_cup -= 1
                if destination_cup < lowest:
                    destination_cup = highest
            for number in cycle(numbers):
                if number == destination_cup:
                    index = numbers.index(number)
                    break
        numbers.insert(index + 1, f)
        numbers.insert(index + 2, s)
        numbers.insert(index + 3, t)
        print("destination: ", destination_cup)
        print("current number: ", current_number)
        current_number_index = numbers.index(current_number)
        numbers = (
            numbers[current_number_index - i :] + numbers[: current_number_index - i]
        )
        i += 1
        i = i % len(numbers)
        counter += 1
    print(numbers)