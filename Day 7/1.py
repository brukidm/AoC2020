import re

bags_list = set()

def search_for_bags(rules, bag, total):
    regex = r"[1-9]* " + bag + r" bag"
    for i in range(len(rules)):
        if re.search(regex, rules[i]):
            new_bag = rules[i].split(" ")[0] + " " + rules[i].split(" ")[1]
            bags_list.add(new_bag)
            search_for_bags(rules, new_bag, total)
        else:
            continue
    return total


with open(r"input") as f:
    lines = f.read().split("\n")
    total = search_for_bags(lines, "shiny gold", 0)
    print(len(bags_list))
