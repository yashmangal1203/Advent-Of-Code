with open("2024\Day1\input.txt") as input:
    puzzleinput = input.read().split()

left_list = sorted([int(j) for i, j in enumerate(puzzleinput) if i % 2 == 0])
right_list = sorted([int(j) for i, j in enumerate(puzzleinput) if i % 2 != 0])

sum1 = 0

for i in left_list:
    sum1 += i * right_list.count(i)
    

print(sum1)
