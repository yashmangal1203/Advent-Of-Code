with open("2015\Day3\input.txt") as input:
    puzzleinput = input.read()


location = [[0, 0], [0, 0]]  # [0] is for Santa and [1] is for RoboSanta
visitedloc = []

for position, move in enumerate(puzzleinput, start=1):
    if position % 2 == 0:
        if move == ">":
            location[1][0] += 1
        elif move == "<":
            location[1][0] -= 1
        elif move == "^":
            location[1][1] += 1
        elif move == "v":
            location[1][1] -= 1

        if location[1] not in visitedloc:
            visitedloc.append(list(location[1]))
    else:
        if move == ">":
            location[0][0] += 1
        elif move == "<":
            location[0][0] -= 1
        elif move == "^":
            location[0][1] += 1
        elif move == "v":
            location[0][1] -= 1

        if location[0] not in visitedloc:
            visitedloc.append(list(location[0]))

print(len(visitedloc))  # 2639
