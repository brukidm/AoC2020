from copy import deepcopy


def play_game(deck_1, deck_2):
    all_combinations = {}
    while len(deck_1) > 0 and len(deck_2) > 0:
        if tuple(deck_1 + [0] + deck_2) in all_combinations:
            return 1
        all_combinations[tuple(deck_1 + [0] + deck_2)] = True

        card_1 = deck_1.pop(0)
        card_2 = deck_2.pop(0)

        if len(deck_1) >= int(card_1) and len(deck_2) >= int(card_2):
            new_deck_1 = deepcopy(deck_1)
            new_deck_2 = deepcopy(deck_2)
            winner = play_game(new_deck_1[0 : int(card_1)], new_deck_2[0 : int(card_2)])
            if winner == 1:
                deck_1.append(card_1)
                deck_1.append(card_2)
            elif winner == 2:
                deck_2.append(card_2)
                deck_2.append(card_1)
        else:
            if int(card_1) > int(card_2):
                deck_1.append(card_1)
                deck_1.append(card_2)
            else:
                deck_2.append(card_2)
                deck_2.append(card_1)
    return 1 if len(deck_1) else 2


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

    winner = play_game(deck_1, deck_2)
    winning_deck = deck_1 if winner == 1 else deck_2

    total = 0
    multiplier = 1

    winning_deck.reverse()

    for points in winning_deck:
        total += multiplier * int(points)
        multiplier += 1
    print(total)