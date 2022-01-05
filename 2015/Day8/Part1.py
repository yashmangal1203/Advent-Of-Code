with open("2015\Day8\input.txt") as input:
    puzzleinput = input.read()
    puzzleinput = puzzleinput.split("\n")

result = 0
for string in puzzleinput:
    result += len(string) - len(eval(string))

print(result)
