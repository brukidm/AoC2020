def get_loops(key, subject_number):
    loop_number = 1
    value = 1
    while True:
        value *= subject_number
        value = value % 20201227
        if value == card_key:
            break
        loop_number += 1
    return loop_number

with open(r"input") as f:
    lines = f.read().split("\n")
    subject_number = 7
    card_key = int(lines[0])
    door_key = int(lines[1])

    card_loops = get_loops(card_key, subject_number)
    door_loops = get_loops(door_key, subject_number)

    value = 1
    for i in range(card_loops):
        value *= door_key
        value = value % 20201227
    print(value)

