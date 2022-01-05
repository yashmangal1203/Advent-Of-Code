with open("2015\\Day9\\input.txt") as input:
    puzzleinput = input.read()
    puzzleinput = puzzleinput.split("\n")

import itertools as it

places = set()
routes = []


for route in puzzleinput:
    source, _, destination, _, dist = route.split()
    places.add(source)
    places.add(destination)
    routes.append(list((source, destination, dist)))
    routes.append(list((destination, source, dist)))

shortestdist = []
shortdist = []
for perm in it.permutations(places):
    for i in range(len(perm) - 1):
        for j in routes:
            if j[0] == perm[i] and j[1] == perm[i + 1]:
                shortdist.append(int(j[2]))
    shortestdist.append(sum(shortdist))
    shortdist = []

print(max(shortestdist)) # Luckily the way my solution is made finding the Shortest(min) and Longest(max) became very easy.
