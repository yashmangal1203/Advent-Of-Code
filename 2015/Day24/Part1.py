with open("2015\\Day24\\input.txt") as input:
    puzzleinput = input.read()
    puzzleinput = puzzleinput.split("\n")
    packages = [int(i) for i in puzzleinput]

import itertools as it
import functools

weight = sum(packages) // 3
qe = []
for i in range(len(packages)):
    for j in it.combinations(packages, i):
        if sum(j) != weight:
            continue
        if len(set(packages) - set(j)) % 2 != 0:
            continue
        qe.append(functools.reduce(lambda x, y: x * y, j, 1))
if qe:
    print(min(qe))  #! 10439961859
