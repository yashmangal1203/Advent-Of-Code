with open("2016\Day1\input.txt") as input:
    puzzleinput = input.read()

x = 0
y = 0

turns = [i.strip() for i in puzzleinput.split(",")]

for turn in turns:
    if turn[0] == "R":
        x, y = -y, x
    else:
        x, y = y, -x

    x += int(turn[1:])

print(abs(x) + abs(y))
