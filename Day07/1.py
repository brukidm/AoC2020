import re

bags_list = set()

def search_for_bags(rules, bag):
    regex = r"[1-9]* " + bag + r" bag"
    for i in range(len(rules)):
        if re.search(regex, rules[i]):
            new_bag = rules[i].split(" ")[0] + " " + rules[i].split(" ")[1]
            bags_list.add(new_bag)
            search_for_bags(rules, new_bag)
        else:
            continue
    return


with open(r"input") as f:
    lines = f.read().split("\n")
    search_for_bags(lines, "shiny gold")
    print(len(bags_list))
