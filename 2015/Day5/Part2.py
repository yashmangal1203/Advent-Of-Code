with open("2015\Day5\input.txt") as input:
    puzzleinput = input.read()


words = puzzleinput.split("\n")

nicewords = 0

for word in words:
    paircondition = False
    lettercondition = False

    pairlist = [word[i] + word[i + 1] for i in range(len(word) - 1)]
    countdict = {}
    for pair in pairlist:
        countdict[pair] = word.count(pair)
    if any(value >= 2 for value in countdict.values()):
        paircondition = True

    for i in range(len(word) - 2):
        if word[i] == word[i + 2]:
            lettercondition = True
            break
    if paircondition and lettercondition:
        nicewords += 1


print(nicewords)  # 69
