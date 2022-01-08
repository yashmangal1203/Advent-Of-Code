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

sue = {}
suecount = {}

for line in puzzleinput:
    line = line.split()
    for j in range(len(line)):
        num = line[1].rstrip(":")
        sue.setdefault(num, {})
        suecount.setdefault(num, 0)
        for i in range(2, 7):
            if line[i].rstrip(":") in tickertape.keys():
                sue[num][line[i].rstrip(":")] = line[i + 1].rstrip(", ")

for key, value in tickertape.items():
    for i in range(1, 501):
        if key in sue[str(i)].keys():
            if key in ["cats", "trees"]:
                if str(value) < sue[str(i)][key]:
                    suecount[str(i)] += 1
            elif key in ["pomeranians", "goldfish"]:
                if str(value) > sue[str(i)][key]:
                    suecount[str(i)] += 1
            else:
                if str(value) == sue[str(i)][key]:
                    suecount[str(i)] += 1


for key, value in suecount.items():
    if value == 3:
        print(key)  #! 323
        break
