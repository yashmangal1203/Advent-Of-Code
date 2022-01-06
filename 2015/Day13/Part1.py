with open("2015\\Day13\\input.txt") as input:
    puzzleinput = input.read()
    puzzleinput = puzzleinput.split("\n")

import itertools as it

attendees = set()

changehappy = []
for i in puzzleinput:
    i = i.split()
    name = i[0]
    attendees.add(name)
    gorl = i[2]
    happiness = int(i[3])
    name2 = i[-1].rstrip(".")
    if gorl == "lose":
        happiness *= -1
    changehappy.append((name, name2, happiness))

sumofhappy = []
totalofhappy = []

for perm in it.permutations(attendees):
    permlist = list(perm)
    permlist.append(permlist[0])  # Adding the first name in the permutation again as the last name to make it a circle.
    for i in range(len(permlist) - 1):
        for j in range(len(changehappy)):
            if permlist[i] == changehappy[j][0] and permlist[i + 1] == changehappy[j][1]:
                sumofhappy.append(changehappy[j][2])
            if permlist[i] == changehappy[j][1] and permlist[i + 1] == changehappy[j][0]:
                sumofhappy.append(changehappy[j][2])
    totalofhappy.append(sum(sumofhappy))
    sumofhappy = []


print(max(totalofhappy))
