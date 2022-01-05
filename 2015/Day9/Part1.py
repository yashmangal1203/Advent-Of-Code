with open("2015\\Day9\\input.txt") as input:
    puzzleinput = input.read()
    puzzleinput = puzzleinput.split("\n")

import itertools as it

places = set()  # A set of all places appearing just once.
routes = []  # A list that will contain all routes + distance in tuples


# ? A loop to create the places set and routes list.
for route in puzzleinput:
    source, _, destination, _, dist = route.split()
    places.add(source)
    places.add(destination)
    routes.append(list((source, destination, dist)))
    routes.append(list((destination, source, dist)))


shortestdist = []  # This list will keep the total distance travelled on every permutation
shortdist = []  # This list will keep all distances of every permutation

# The itertools permutation function is the main method used to find all the possible routes, the following loop does the following:
# 1. The first loop goes over each permutation
# 2. The second loop goes over the places in each permutation
# 3. The third loop goes over our 'Routes' list to find the matching place and adds that distance to the shortdist list.
for perm in it.permutations(places):
    for i in range(len(perm) - 1):
        for j in routes:
            if j[0] == perm[i] and j[1] == perm[i + 1]:
                shortdist.append(int(j[2]))
    shortestdist.append(sum(shortdist))
    shortdist = []

print(min(shortestdist))
