with open("2016\Day2\input.txt") as input:
    puzzleinput = input.read()
    puzzleinput = puzzleinput.split("\n")

keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
position1 = [1, 1]
combination = []

for line in puzzleinput:
    for char in line:
        if char == "D":
            if position1[0] == 2:
                continue
            else:
                position1[0] += 1
        elif char == "L":
            if position1[1] == 0:
                continue
            else:
                position1[1] -= 1
        elif char == "R":
            if position1[1] == 2:
                continue
            else:
                position1[1] += 1
        elif char == "U":
            if position1[0] == 0:
                continue
            else:
                position1[0] -= 1
    combination.append(int(keypad[position1[0]][position1[1]]))


print(combination)
