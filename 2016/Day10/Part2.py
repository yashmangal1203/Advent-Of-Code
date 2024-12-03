bots = {}
output = {}
specialbot = 0
changed = True

with open("2016\Day10\input.txt", "r") as f:
    data = f.read().splitlines()

# Starts by running through the instructions handing out free chips
for line in data:
    if line.startswith("value"):
        line = line.split()
        if int(line[-1]) in bots:
            bots[int(line[-1])].append(int(line[1]))
        else:
            bots[int(line[-1])] = [int(line[1])]

# Keeps running until no more bots have at least 2 chips
while changed:
    changed = False
    # Runs through the instructions to hand out chips from bots with at least 2
    for line in data:
        if line.startswith("bot"):
            line = line.split()

            """ Really ugly and probably bloated code that checks whether the bot mentioned
			has at least 2 chips then checks whether to send those chips to output or another
			bot and then does so in the least elegant way possible"""
            if int(line[1]) in bots.keys() and len(bots[int(line[1])]) >= 2:
                changed = True
                if line[5] == "bot":
                    if int(line[6]) in bots.keys():
                        bots[int(line[6])].append(min(bots[int(line[1])]))
                    else:
                        bots[int(line[6])] = [min(bots[int(line[1])])]
                else:
                    if int(line[6]) in output.keys():
                        output[int(line[6])].append(min(bots[int(line[1])]))
                    else:
                        output[int(line[6])] = [min(bots[int(line[1])])]
                if line[10] == "bot":
                    if int(line[11]) in bots.keys():
                        bots[int(line[11])].append(max(bots[int(line[1])]))
                    else:
                        bots[int(line[11])] = [max(bots[int(line[1])])]
                else:
                    if int(line[11]) in output.keys():
                        output[int(line[11])].append(max(bots[int(line[1])]))
                    else:
                        output[int(line[11])] = [max(bots[int(line[1])])]
                bots[int(line[1])] = []

            """ Checks all the bots after each instruction is run to see if any have both chips 17 and 61
			then stores that bot's number for later"""
            for bot in bots.keys():
                if 17 in bots[bot] and 61 in bots[bot]:
                    specialbot = bot


print(output[0][0] * output[1][0] * output[2][0])
