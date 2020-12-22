from copy import deepcopy

with open(r"input") as f:
    lines = f.read().split("\n")

    deck = []
    for line in lines:
        if "Player" in line:
            continue
        elif not line:
            deck_1 = deepcopy(deck)
            deck.clear()
        else:
            deck.append(line)

    deck_2 = deepcopy(deck)

    while len(deck_1) > 0 and len(deck_2) > 0:
        card_1 = deck_1.pop(0)
        card_2 = deck_2.pop(0)

        if int(card_1) > int(card_2):
            deck_1.append(card_1)
            deck_1.append(card_2)
        else:
            deck_2.append(card_2)
            deck_2.append(card_1)

    winning_deck = deck_1 if len(deck_1) else deck_2

    total = 0
    multiplier = 1

    winning_deck.reverse()

    for points in winning_deck:
        total += multiplier * int(points)
        multiplier += 1
    print(total)