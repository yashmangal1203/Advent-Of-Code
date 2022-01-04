with open("2015\Day6\input.txt") as input:
    puzzleinput = input.read()

instructions = puzzleinput.split("\n")

# ? 0 - OFF and 1 - ON
lightgrid = []
for i in range(1000):
    temp = []
    for j in range(1000):
        temp.append(0)
    lightgrid.append(temp)


for instruction in instructions:
    instruc = instruction.split()
    if instruc[0] == "toggle":
        lcornerx = int(instruc[1].split(",")[0])
        lcornery = int(instruc[1].split(",")[1])
        rcornerx = int(instruc[3].split(",")[0])
        rcornery = int(instruc[3].split(",")[1])
    else:
        lcornerx = int(instruc[2].split(",")[0])
        lcornery = int(instruc[2].split(",")[1])
        rcornerx = int(instruc[4].split(",")[0])
        rcornery = int(instruc[4].split(",")[1])

    for i in range(lcornerx, rcornerx + 1):
        for j in range(lcornery, rcornery + 1):
            if instruction.startswith("turn on"):
                lightgrid[i][j] += 1
            elif instruction.startswith("turn off"):
                if lightgrid[i][j] > 0:
                    lightgrid[i][j] -= 1

            elif instruction.startswith("toggle"):
                lightgrid[i][j] += 2

lightslit = 0

for i in range(1000):
    lightslit += sum(lightgrid[i])
print(lightslit)  # 17836115
