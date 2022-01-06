with open("2015\\Day13\\input.txt") as input:
    puzzleinput = input.read()
    puzzleinput = puzzleinput.split("\n")

import itertools as it # This module is required for maknig permutations

attendees = set()
me = "me" # As part of part 2, adding yourself to the attendees list.
attendees.add(me)

changehappy = [] 
for i in puzzleinput:
    i = i.split()
    name = i[0]
    attendees.add(name) # Making the attendee set for unique names
    gorl = i[2]
    happiness = int(i[3])
    name2 = i[-1].rstrip(".")
    if gorl == "lose": 
        happiness *= -1
    changehappy.append((name, name2, happiness))
    changehappy.append((name, me, 0)) # Adding yourself to the happiness
    changehappy.append((me, name2, 0))

changehappy = list(set(changehappy)) # To remove repeated names.
sumofhappy = []
totalofhappy = []

for perm in it.permutations(attendees):
    permlist = list(perm)
    permlist.append(permlist[0]) 
    for i in range(len(permlist) - 1):
        for j in range(len(changehappy)):
            if permlist[i] == changehappy[j][0] and permlist[i + 1] == changehappy[j][1]:
                sumofhappy.append(changehappy[j][2])
            if permlist[i] == changehappy[j][1] and permlist[i + 1] == changehappy[j][0]:
                sumofhappy.append(changehappy[j][2])
    totalofhappy.append(sum(sumofhappy))
    sumofhappy = []


print(max(totalofhappy))  #! 725
