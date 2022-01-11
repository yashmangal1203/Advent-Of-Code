with open("2015\\Day24\\input.txt") as input:
    puzzleinput = input.read()
    puzzleinput = puzzleinput.split("\n")
    packages = [int(i) for i in puzzleinput]

import itertools as it
import functools

weight = sum(packages) // 4
qe = []
for i in range(len(packages)):
    for j in it.combinations(packages, i):
        if sum(j) != weight:
            continue
        qe.append(functools.reduce(lambda x, y: x * y, j, 1))
if qe:
    print(min(qe)) #! 72050269
