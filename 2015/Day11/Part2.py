def is_valid(s):
    condition2 = False
    condition3 = False

    if any(c in s for c in "iol"):
        return False

    straightchar = [str(chr(i) + chr(i + 1) + chr(i + 2)) for i in range(97, 121)]
    for char in straightchar:
        if char in s:
            condition2 = True

    pairchar = [str(chr(i) + chr(i)) for i in range(97, 123)]
    countdict = {}
    for pair in pairchar:
        countdict[pair] = s.count(pair)
    if sum(countdict.values()) > 1:
        condition3 = True

    return all([condition2, condition3])


def shift(s):
    data = list(s)
    for i in range(len(data) - 1, -1, -1):
        data[i] = chr((ord(data[i]) - ord("a") + 1) % 26 + ord("a"))
        if data[i] != "a":
            break
    return "".join(data)


puzzleinput = shift("cqjxxyzz")  # One shift and then continue checking.
while not is_valid(puzzleinput):
    puzzleinput = shift(puzzleinput)

print(puzzleinput)  #! cqkaabcc
