def count_options(index, nodes, lookup):
    result = 0

    indexes_to_visit = []
    if index not in lookup:
        for i in range(index + 1, index + 4):
            if i < len(nodes):
                if nodes[i] - nodes[index] in (1, 2, 3):
                    indexes_to_visit.append(i)
            else:
                break

        if indexes_to_visit:
            for index_to_visit in indexes_to_visit:
                result += count_options(index_to_visit, nodes, lookup)
            lookup[index] = result
        else:
            return 1
    return lookup[index]


lookup = {}

with open(r"input") as f:
    lines = [int(x) for x in f.read().split("\n")]
    lines.sort()
    lines.append(lines[-1] + 3)
    lines.insert(0, 0)

    print(count_options(0, lines, lookup))
    print(lookup)