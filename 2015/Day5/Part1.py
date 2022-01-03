with open("2015\Day5\input.txt") as input:
    puzzleinput = input.read()

words = puzzleinput.split("\n")

vowels = ["a", "e", "i", "o", "u"]

nicewords = 0

for word in words:
    vowelcondition = False
    lettercondition = True
    dlettercondition = False

    vowelcount = word.count("a") + word.count("e") + word.count("i") + word.count("o") + word.count("u")
    if vowelcount >= 3:
        vowelcondition = True

    for s in ["ab", "cd", "pq", "xy"]:
        if s in word:
            lettercondition = False
            break

    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            dlettercondition = True
            break
    if vowelcondition and dlettercondition and lettercondition:
            nicewords += 1


print(nicewords)  # 238
