screen = [[0] * 50 for _ in range(6)]

#! mY SOLUTIION COULDN'T GET THE ANSWER AND I TRIED MY BEST TO FIGURE OUT WHY, IN THE END HAD TO USE r/glenbolake


def rect(a, b):
    for r in range(b):
        for c in range(a):
            screen[r][c] = 1


def print_grid(screen):
    print("Printing ...")
    for i in range(6):
        for j in range(50):
            print(screen[i][j], end="")
        print()


def rotate(how, which, amount):
    if how == "row":
        screen[which] = screen[which][-amount:] + screen[which][:-amount]
    else:  # how == 'column'
        prev = [screen[r][which] for r in range(6)]
        for r in range(6):
            screen[r][which] = prev[r - amount]


with open("2016\Day8\input.txt") as f:
    instr = f.read().splitlines()

for line in instr:
    command = line.split()
    if command[0] == "rect":
        rect(*map(int, command[1].split("x", 1)))
        print_grid(screen)
        print(sum(sum(line) for line in screen))
    else:  # command[0] == 'rotate':
        rotate(command[1], int(command[2].split("=")[1]), int(command[4]))
        print_grid(screen)
        print(sum(sum(line) for line in screen))

trans = str.maketrans("01", " #")
print("\n".join(["".join(map(str, line)) for line in screen]).translate(trans))
