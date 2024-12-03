import re

with open("2024\Day3\input.txt") as input:
    puzzleinput = input.read()

pattern = re.compile("mul\(\d{1,3},\d{1,3}\)")
sum = 0
for instruction in pattern.findall(puzzleinput):
    numbers = re.findall("\d{1,3}", instruction)
    sum += int(numbers[0]) * int(numbers[1])

# print(pattern.findall(puzzleinput))
print(sum)
