with open("2015\\Day17\\input.txt") as input:
    puzzleinput = input.read()
    puzzleinput = puzzleinput.split("\n")

import itertools as it

containers = [int(i) for i in puzzleinput]
possibilities = 0

for i in range(1, len(containers)):
    subtotal = 0
    for perm in it.combinations(containers, i):
        if sum(perm) == 150:
            subtotal += 1
            possibilities += 1
    print(i, subtotal, possibilities) #! 15
