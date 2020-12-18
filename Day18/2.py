def is_greater_precedence(op1, op2):
    pre = {"+": 1, "*": 0}
    return pre[op1] >= pre[op2]


def evalPostfix(text):
    s = []
    for symbol in text:
        try:
            result = int(symbol)
        except ValueError:
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
                while (
                    operator_stack
                    and operator_stack[-1] != "("
                    and is_greater_precedence(operator_stack[-1], token)
                ):
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
        operator_stack.reverse()
        output_queue += operator_stack
        total += evalPostfix(output_queue)
        print(output_queue)
    print(total)
