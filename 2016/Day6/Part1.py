with open("2016\Day6\input.txt") as input:
    puzzleinput = input.read()
    puzzleinput = puzzleinput.split("\n")

code = ""

for i in range(8):
    countdict = {}
    for char in [j[i] for j in puzzleinput]:
        countdict.setdefault(char, 0)
        countdict[char] += 1
    sorted_dict = sorted(countdict.items(), key=lambda x: (-x[1], x[0]))
    code += str(sorted_dict[0][0])

print(code)
