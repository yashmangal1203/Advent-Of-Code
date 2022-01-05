with open("2015\Day7\input.txt") as input:
    puzzleinput = input.read()


instructions = puzzleinput.split("\n")

# Initializing a dictionary with "" for all the wires
inputs = {}

for temp1 in instructions:
    temp1 = temp1.split(" -> ")
    inputs[temp1[-1]] = ""

count = 0

while "" in inputs.values():  # so that we don't stop after one loop because input.txt is unordered.
    for instruction in instructions:
        instruction = instruction.split(" -> ")
        temp = instruction[0].split()  # splitting the left side of connectors

        if len(temp) == 1:  # For those connections like , '123 -> x'
            loperand = temp[0] if temp[0].isdigit() else inputs[temp[0]]  # 123
            inputs[instruction[-1]] = loperand  # {'x':''} to {'x':123}
            continue  # skip the rest of the loop
        else:  # For other situations
            if temp[0] == "NOT":  # Special Condition to check because then temp list is one len() short
                operator = temp[0]
                loperand = temp[1] if temp[1].isdigit() else inputs[temp[1]]
            else:
                operator = temp[1]
                loperand1 = temp[0] if temp[0].isdigit() else inputs[temp[0]]
                loperand2 = temp[2] if temp[2].isdigit() else inputs[temp[2]]

        # Doing the bitwise operations:
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

print(inputs["a"])  # 46065
