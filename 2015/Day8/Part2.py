with open("2015\Day8\input.txt") as input:
    puzzleinput = input.read()
    puzzleinput = puzzleinput.split("\n")

sum1 = 0

for string in puzzleinput:
    sum1 += 2
    sum1 += string.count('"')
    sum1 += string.count("\\")

print(sum1)  # 2085
