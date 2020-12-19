import regex as re

with open(r"input") as f:
    lines = f.read().split("\n")

    grammar = {}

    i = 0
    while True:
        if not lines[i]:
            break
        key, rule = lines[i].split(" ", 1)
        if any(char.isdigit() for char in rule):
            if "|" in rule:
                grammar[key[:-1]] = "(" + rule + ")"
            else:
                grammar[key[:-1]] = rule
        else:
            grammar[key[:-1]] = rule[1]
        i += 1

    i += 1
    grammar["8"] = "42+"
    grammar[
        "11"
    ] = "(42{c}31{c}|42{d}31{d}|42{e}31{e}|42{f}31{f}|42{g}31{g}|42{h}31{h}|42{i}31{i}|42{j}31{j}|42{k}31{k}|42{l}31{l}|42{m}31{m})"
    regex_pattern = grammar["0"]

    while True:
        m = re.search("\d+", regex_pattern)
        if not m:
            break
        else:
            if not m:
                break
            regex_pattern = regex_pattern.replace(m.group(0), grammar[m.group(0)], 1)
    regex_pattern = regex_pattern.replace(" ", "")
    regex_pattern = "^" + regex_pattern + "$"
    regex_pattern = regex_pattern.replace("c", "1").replace("d", "2").replace("e", "3").replace(
        "f", "4"
    ).replace("g", "5").replace("h", "6").replace("i", "7").replace("j", "8").replace(
        "k", "9"
    ).replace(
        "l", "10"
    ).replace(
        "m", "11"
    )
    print(regex_pattern)
    total = 0
    while i < len(lines):
        if re.match(regex_pattern, lines[i]):
            total += 1
        i += 1
    print(total)
