import re

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
    regex_pattern = grammar['0']
    while True:
        m = re.search('\d+', regex_pattern)
        if not m:
            break
        else:
            regex_pattern = regex_pattern.replace(m.group(0), grammar[m.group(0)], 1)
    regex_pattern = regex_pattern.replace(" ", "")
    print(regex_pattern)
    regex_pattern = "^" + regex_pattern + "$"
    total = 0
    while i < len(lines):
        if re.match(regex_pattern, lines[i]):
            total += 1
        i += 1
    print(total)