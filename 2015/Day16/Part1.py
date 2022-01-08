with open("2015\\Day16\\input.txt") as input:
    puzzleinput = input.read()
    puzzleinput = puzzleinput.split("\n")

tickertape = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}

sue = {}  # details of each aunt sue with their compounds
suecount = {}  # To keep the count of how many compunds match with ticker


for line in puzzleinput:
    line = line.split()
    for j in range(len(line)):
        num = line[1].rstrip(":")
        sue.setdefault(num, {})
        suecount.setdefault(num, 0)
        for i in range(2, 7):
            if line[i].rstrip(":") in tickertape.keys():
                sue[num][line[i].rstrip(":")] = line[i + 1].rstrip(", ")

"""
Here's what my solution is based on:
1. Tickertapes keys and values are compared to the keys and values of all aunt sues.
2. If that key is in that aunt sue keys then values are checked.
3. If values are same then that aunt sue's count is +1.
4. After all keys values and all aunt sues are checked, the final values of suecount is checked.
5. If any value is 3!, then that is our answer.

"""

for key, value in tickertape.items():
    for i in range(1, 501):
        if key in sue[str(i)].keys():
            if str(value) == sue[str(i)][key]:
                suecount[str(i)] += 1

for key, value in suecount.items():
    if value == 3:
        print(key)  #! 213
        break
