#! I take no credit for this solution, all belongs on r/alphazero924. Link to his github - 'https://github.com/drathke924/userscripts/blob/master/Advent_of_Code_2016/10.py'

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

print(specialbot)


#! I couldn't see the problem in my solution so had to use a redditors solution. This below is my solution.

# with open("2016\Day10\input.txt") as input:
#     puzzleinput = input.read()
#     puzzleinput = puzzleinput.split("\n")


# # puzzleinput = [
# #     "value 5 goes to bot 2",
# #     "bot 2 gives low to bot 1 and high to bot 0",
# #     "value 3 goes to bot 1",
# #     "value 3 goes to bot 1",
# #     "value 2 goes to bot 2",
# #     "bot 1 gives low to output 1 and high to bot 0",
# #     "value 5 goes to bot 2",
# #     "bot 0 gives low to output 2 and high to output 0",
# #     "value 2 goes to bot 2",
# # ]

# who_gives_who = {}
# bots = {}

# for line in puzzleinput:
#     line = line.split()
#     bots.setdefault(line[1], [])
#     if line[0] == "bot":
#         who_gives_who.setdefault(line[1], {"low": 0, "high": 0})
#         who_gives_who[line[1]]["low"] = str(line[5] + " " + line[6])
#         who_gives_who[line[1]]["high"] = str(line[-2] + " " + line[-1])


# line_completed = []
# print(who_gives_who)
# # print(bots)


# def two_values(bots):
#     for key, value in bots.items():
#         if len(value) < 2:
#             print(key)
#             return True
#     return False


# while two_values(bots):
#     for line_num, line in enumerate(puzzleinput):
#         line = line.split()
#         if '30' in line:
#             print(True)
#         if line not in line_completed and line[0] == "value":
#             bots[line[-1]].append(int(line[1]))
#             line_completed.append(line_num)
#         elif line[0] == "bot":
#             try:
#                 if line_num not in line_completed:
#                     if "output" not in line:
#                         try:
#                             bots[line[6]].append(min(bots[line[1]]))
#                             bots[line[-1]].append(max(bots[line[1]]))
#                             line_completed.append(line_num)
#                         except:
#                             continue
#                     else:
#                         if line[5] == "output":
#                             line_completed.append(line_num)
#                             continue
#                             try:
#                                 bots[line[1]].remove(min(bots[line[1]]))
#                             except:
#                                 continue
#                         # else:
#                         #     try:
#                         #         bots[line[1]].remove(max(bots[line[1]]))
#                         #     except:
#                         #         continue

#                 else:
#                     continue
#             except:
#                 continue

# print(bots)
