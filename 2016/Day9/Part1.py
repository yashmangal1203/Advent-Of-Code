with open("2016\Day9\input.txt") as input:
    puzzleinput = input.read()

number = 0
while "(" in puzzleinput:
    number += puzzleinput.find("(")
    puzzleinput = puzzleinput[puzzleinput.find("(") :]
    marker_string = puzzleinput[1 : puzzleinput.find(")")].split("x")
    puzzleinput = puzzleinput[puzzleinput.find(")") + 1 :]
    number += len(puzzleinput[: int(marker_string[0])]) * int(marker_string[1])
    puzzleinput = puzzleinput[int(marker_string[0]) :]

number += len(puzzleinput)

print(number)
