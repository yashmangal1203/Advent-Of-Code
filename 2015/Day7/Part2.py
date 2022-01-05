with open("2015\Day7\input.txt") as input:
    puzzleinput = input.read()


instructions = puzzleinput.split("\n")
instructions.append("46065 -> b") # Part 2 says to get the Part 1 signal of 'a' and assign it to 'b'. so I added this in the end of the main input. 

inputs = {}

for temp1 in instructions:
    temp1 = temp1.split(" -> ")
    inputs.setdefault(temp1[-1], "")

bcount = 0
count = 0

while "" in inputs.values():
    for instruction in instructions:
        instruction = instruction.split(" -> ")
        temp = instruction[0].split()
        if len(temp) == 1:
            loperand = temp[0] if temp[0].isdigit() else inputs[temp[0]]
            inputs[instruction[-1]] = loperand
            continue
        else:
            if temp[0] == "NOT":
                operator = temp[0]
                loperand = temp[1] if temp[1].isdigit() else inputs[temp[1]]
            else:
                operator = temp[1]
                loperand1 = temp[0] if temp[0].isdigit() else inputs[temp[0]]
                loperand2 = temp[2] if temp[2].isdigit() else inputs[temp[2]]

        if operator == "NOT" and not loperand == "":
            inputs[instruction[-1]] = str(~int(loperand))
        elif operator != "NOT" and not loperand1 == "" and not loperand2 == "":
            if operator == "AND":
                inputs[instruction[-1]] = int(loperand1) & int(loperand2)
            elif operator == "LSHIFT":
                inputs[instruction[-1]] = int(loperand1) << int(loperand2)
            elif operator == "RSHIFT":
                inputs[instruction[-1]] = int(loperand1) >> int(loperand2)
            elif operator == "OR":
                inputs[instruction[-1]] = int(loperand1) | int(loperand2)
        else:
            continue

print(inputs["a"])
