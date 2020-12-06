with open(r"input") as f:
    lines = f.read().split('\n')
    answers = set()
    total_answers = list()
    for line in lines:
        if line != "":
            for char in line:
                answers.add(char)
        else:
            total_answers.append(len(answers))
            answers.clear()
    result = sum(total_answers)
    print(result)
