import re

def search_for_bags(rules, bag, total):
    regex = bag + r" bags contain"
    total = 0
    for i in range(len(rules)):
        if re.search(regex, rules[i]):
            bags = rules[i].replace(regex, "")
            bags = bags[:-1].split(", ")
            for bag in bags:
                if not "no other" in bag:
                    bag = bag.strip().replace(" bags", "").replace(" bag", "")
                    amount_of_bags = int(bag.split(" ")[0])
                    bag_name = bag.split(" ", 1)[1]
                    total += amount_of_bags + amount_of_bags * search_for_bags(rules, bag_name, total)
                else:
                    return 0
    return total

with open(r"input") as f:
    lines = f.read().split("\n")
    total = search_for_bags(lines, "shiny gold", -1)
    print(total)