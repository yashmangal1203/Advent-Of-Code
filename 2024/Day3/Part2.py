import re

with open("2024\Day3\input.txt") as input:
    puzzleinput = input.read()

pattern = re.compile("mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)")
sum = 0
dont = False

for instruction in pattern.findall(puzzleinput):
    if instruction == "don't()":
        dont = True
        continue
    elif instruction == "do()":
        dont = False
        continue

    if not dont:
        numbers = re.findall("\d{1,3}", instruction)

        sum += int(numbers[0]) * int(numbers[1])

print(sum)
