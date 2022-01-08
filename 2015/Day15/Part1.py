with open("2015\\Day15\\input.txt") as input:
    puzzleinput = input.read()
    puzzleinput = puzzleinput.split("\n")

import itertools as it

ingredients = {}
ingredients1 = set()

for ingre in puzzleinput:
    ingre = ingre.split()
    ingredients1.add(ingre[0][:-1])
    ingredients.setdefault(ingre[0][:-1], {"capacity": 0, "durab": 0, "flavor": 0, "texture": 0, "calories": 0})
    ingredients[ingre[0][:-1]]["capacity"] = int(ingre[2][:-1])
    ingredients[ingre[0][:-1]]["durab"] = int(ingre[4][:-1])
    ingredients[ingre[0][:-1]]["flavor"] = int(ingre[6][:-1])
    ingredients[ingre[0][:-1]]["texture"] = int(ingre[8][:-1])
    ingredients[ingre[0][:-1]]["calories"] = int(ingre[-1])

score = []

"""
This does the following:
1. Permutations are used to find a tuple of combination of numbers haing a sum of 100
3. Loop goes ahead only if sum of that permutation is 100 beacause total teaspoons available are only 100
4. total properties are set to 0 at the beginning of every permutation
5. Properties of every ingredient are added up and then checked if any of them is 0 to stop the loop and not add to our score list
6. Then max of our scorelist is preinted.
"""

for perm in it.permutations(range(1, 100), len(ingredients1)):
    if sum(perm) == 100:
        cap, dur, fla, tex = 0, 0, 0, 0
        for ing, permn in zip(ingredients1, range(len(ingredients1))):
            cap += ingredients[ing]["capacity"] * perm[permn]
            dur += ingredients[ing]["durab"] * perm[permn]
            fla += ingredients[ing]["flavor"] * perm[permn]
            tex += ingredients[ing]["texture"] * perm[permn]
        if cap > 0 and dur > 0 and fla > 0 and tex > 0:
            score.append(int(cap * dur * fla * tex))

print(max(score))  #!13882464
