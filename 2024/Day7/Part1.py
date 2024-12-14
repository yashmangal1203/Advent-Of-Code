import itertools

with open("2024\Day7\input.txt") as input:
    input_read = input.read().split("\n")
    puzzleinput = {}
    for i in input_read:
        puzzleinput[i.split(":")[0]] = i.split(":")[1].split()

math_operations = ["+", "*"]


def solve_equation(equation):
    answer = 0
    for i, operation in enumerate(equation):
        if operation == "+":
            if answer == 0:
                answer += int(equation[i - 1]) + int(equation[i + 1])
            else:
                answer += int(equation[i + 1])
        elif operation == "*":
            if answer == 0:
                answer += int(equation[i - 1]) * int(equation[i + 1])
            else:
                answer *= int(equation[i + 1])
        else:
            continue
    return str(answer)


def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    # Recipe credited to George Sakkis
    num_active = len(iterables)
    nexts = itertools.cycle(iter(it).__next__ for it in iterables)
    while num_active:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            # Remove the iterator we just exhausted from the cycle.
            num_active -= 1
            nexts = itertools.cycle(itertools.islice(nexts, num_active))


calibration_result = 0

for i, j in list(puzzleinput.items()):
    math_operations = [i for i in itertools.product(["+", "*"], repeat=len(j) - 1)]
    equations = []

    for m in math_operations:
        equations.append(list(roundrobin(j, m)))
    solved = False
    for eq in equations:
        if not solved:
            equation_answer = solve_equation(eq)
            if equation_answer == i:
                calibration_result += int(equation_answer)
                solved = True

print(calibration_result)
