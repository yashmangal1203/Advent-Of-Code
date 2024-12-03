with open("2024\Day1\input.txt") as input:
    puzzleinput = input.read().split()

left_list = sorted([int(j) for i, j in enumerate(puzzleinput) if i % 2 == 0])
right_list = sorted([int(j) for i, j in enumerate(puzzleinput) if i % 2 != 0])

sum1 = 0

for i, j in zip(left_list, right_list):
    sum1 += abs(i - j)

print(sum1)
