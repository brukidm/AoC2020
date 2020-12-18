def evalPostfix(text):
    s = []
    for symbol in text:
        try:
            result = int(symbol)
        except ValueError:
            if symbol not in "+*":
                raise ValueError("text must contain only numbers and operators")
            result = eval("%d %s %d" % (s.pop(), symbol, s.pop()))
        s.append(result)
    return s.pop()


with open(r"input") as f:
    lines = f.read().split("\n")

    total = 0
    for line in lines:
        line = line.replace("(", "( ").replace(")", " )")
        tokens = line.split(" ")

        output_queue = []
        operator_stack = []

        for token in tokens:
            if token.isdigit():
                output_queue.append(token)
            elif token in ["+", "*"]:
                while len(operator_stack) > 0 and operator_stack[-1] != "(":
                    pop = operator_stack.pop()
                    output_queue.append(pop)
                operator_stack.append(token)
            elif token == "(":
                operator_stack.append(token)
            elif token == ")":
                while operator_stack and operator_stack[-1] != "(":
                    pop = operator_stack.pop()
                    output_queue.append(pop)
                if operator_stack[-1] == "(":
                    operator_stack.pop()
        for operator in operator_stack:
            pop = operator_stack.pop()
            output_queue.append(pop)
        total += evalPostfix(output_queue)
    print(total)
