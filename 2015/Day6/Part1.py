with open("2015\Day6\input.txt") as input:
    puzzleinput = input.read()

instructions = puzzleinput.split("\n")

# Making the main light grid with nested loops.
lightgrid = []
for i in range(1000):
    temp = []
    for j in range(1000):
        temp.append(0)
    lightgrid.append(temp)

# Main loop that will loop over all different inputs.
for instruction in instructions:
    instruc = instruction.split()  # to split the instruction and co-ordinates.

    # Making variables for the co-ordinates
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

    # Second main loop to switch lights in the grid.
    for i in range(lcornerx, rcornerx + 1):
        for j in range(lcornery, rcornery + 1):
            if instruction.startswith("turn on"):
                lightgrid[i][j] = 1
            elif instruction.startswith("turn off"):
                lightgrid[i][j] = 0
            elif instruction.startswith("toggle"):
                if lightgrid[i][j] == 0:
                    lightgrid[i][j] = 1
                else:
                    lightgrid[i][j] = 0

lightslit = 0

# A short loop to find the number of lights lit.
for i in range(1000):
    lightslit += lightgrid[i].count(1)

print(lightslit)  # 59999
