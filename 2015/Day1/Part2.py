with open('2015\Day1\input.txt') as input:
    puzzleinput = input.read()

level = 0

for position, char in enumerate(puzzleinput):
    if level == -1:
        break

    if char == '(':
        level += 1
    else:
        level -= 1


print(position)  # 1795
