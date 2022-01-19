with open("2016\Day3\input.txt") as input:
    puzzleinput = input.read()
    puzzleinput = puzzleinput.split("\n")

possible = 0

for line in puzzleinput:
    side = sorted(list(map(int, line.split())))
    if side[0] + side[1] > side[2]:
        possible += 1

print(possible)
