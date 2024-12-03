from collections import Counter

with open("2024\Day2\input.txt") as input:
    puzzleinput = input.read().split("\n")

safe = 0

for report in puzzleinput:
    levels = [int(i) for i in report.split()]
    if list(Counter(levels).values()).count(1) < len(levels):
        continue
    ascending_levels = sorted(levels)
    descending_levels = sorted(levels, reverse=True)
    if levels == ascending_levels or levels == descending_levels:
        differences = [abs(levels[i] - levels[i + 1]) for i in range(len(levels) - 1)]
        if (max(differences)) <= 3:
            safe += 1


print(safe)
