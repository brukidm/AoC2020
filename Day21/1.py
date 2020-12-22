ingredients = {}
compare_ingrs = []
compare_alergs = []

with open(r"input") as f:
    lines = f.read().split("\n")
    for line in lines:
        line = line.split("(contains")
        ingrs = line[0][:-1].split(" ")
        compare_ingrs.append(ingrs)
        alergs = line[1].replace(")", "").strip().split(", ")
        compare_alergs.append(alergs)
        for ingr in ingrs:
            if ingr not in ingredients:
                ingredients[ingr] = set()
            for alerg in alergs:
                ingredients[ingr].add(alerg)

    ingr_appearances = {}
    for ingredient in ingredients:
        i = 0
        appearances = {}
        for line in lines:
            for alergen in ingredients[ingredient]:
                if alergen in compare_alergs[i] and ingredient in compare_ingrs[i]:
                    if alergen not in appearances:
                        appearances[alergen] = 1
                    else:
                        appearances[alergen] += 1
            i += 1
        ingr_appearances[ingredient] = appearances

    alerg_appearances = {}
    for alerg_list in compare_alergs:
        for alerg in alerg_list:
            if alerg not in alerg_appearances:
                alerg_appearances[alerg] = 1
            else:
                alerg_appearances[alerg] += 1

    impossible = set()
    for ingr in ingr_appearances:
        impossible_check = True
        for alerg in ingr_appearances[ingr]:
            if ingr_appearances[ingr][alerg] == alerg_appearances[alerg]:
                impossible_check = False
        if impossible_check:
            impossible.add(ingr)

    total = 0
    for ingredient in impossible:
        for l in compare_ingrs:
            for c in l:
                if c == ingredient:
                    total += 1
    print(total)