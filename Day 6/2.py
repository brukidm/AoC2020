with open(r"input") as f:
    lines = f.read().split('\n')
    total_answers = list()
    group_answers = list()
    for line in lines:
        if line != "":
            answers = [char for char in line]
            group_answers.append(answers)
        else:
            total_answers.append(len(set.intersection(*map(set,group_answers))))
            group_answers.clear()
    result = sum(total_answers)
    print(result)
