with open("2016\Day9\input.txt") as input:
    puzzleinput = input.read()


def decomp(string1):
    if "(" not in string1:
        return len(string1)
    number = 0
    while "(" in string1:
        number += string1.find("(")
        string1 = string1[string1.find("(") :]
        marker = string1[1 : string1.find(")")].split("x")
        string1 = string1[string1.find(")") + 1 :]
        number += decomp(string1[: int(marker[0])]) * int(marker[1])
        string1 = string1[int(marker[0]) :]
    number += len(string1)
    return number


print(decomp(puzzleinput))
