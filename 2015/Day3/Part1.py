with open('2015\Day3\input.txt') as input:
    puzzleinput = input.read()

location = [0, 0]
visitedloc = [[0, 0]]

for move in puzzleinput:
    if move == '>':
        location[0] += 1
    elif move == '<':
        location[0] -= 1
    elif move == '^':
        location[1] += 1
    elif move == 'v':
        location[1] -= 1

    if location not in visitedloc:
        visitedloc.append(list(location))

print(len(visitedloc)) # 2565
