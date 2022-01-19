with open("2016\Day3\input.txt") as input:
    puzzleinput = input.read()
    puzzleinput = puzzleinput.split("\n")

possible = 0
triangles = [list(map(int, i.split())) for i in puzzleinput]

side1 = [i[0] for i in triangles]
side2 = [i[1] for i in triangles]
side3 = [i[2] for i in triangles]

for i in range(len(side1) - 3):
    side = sorted(side1[:3])
    side1 = side1[3:]
    if side[0] + side[1] > side[2]:
        possible += 1
    if side1 == []:
        break

for i in range(len(side2) - 3):
    side = sorted(side2[:3])
    side2 = side2[3:]
    if side[0] + side[1] > side[2]:
        possible += 1
    if side2 == []:
        break

for i in range(len(side3) - 3):
    side = side3[:3]
    side3 = side3[3:]
    side = sorted(side)
    if side[0] + side[1] > side[2]:
        possible += 1
    if side3 == []:
        break

print(possible)
