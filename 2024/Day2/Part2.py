from collections import Counter

with open("2024\Day2\input.txt") as input:
    puzzleinput = input.read().split("\n")

safe = 0

for report in puzzleinput:
    marked_safe = False
    levels = [int(i) for i in report.split()]
    ascending_levels = sorted(levels)
    descending_levels = sorted(levels, reverse=True)
    differences = [abs(levels[i] - levels[i + 1]) for i in range(len(levels) - 1)]

    if (
        not (list(Counter(levels).values()).count(1) < len(levels))
        and (levels == ascending_levels or levels == descending_levels)
        and max(differences) <= 3
    ):
        safe += 1
        marked_safe = True
        continue
    else:
        for i in range(len(levels)):
            temp_levels = levels.copy()
            temp_levels.pop(i)

            ascending_levels = sorted(temp_levels)
            descending_levels = sorted(temp_levels, reverse=True)
            differences = [
                abs(temp_levels[i] - temp_levels[i + 1])
                for i in range(len(temp_levels) - 1)
            ]

            if (
                not (list(Counter(temp_levels).values()).count(1) < len(temp_levels))
                and (
                    temp_levels == ascending_levels or temp_levels == descending_levels
                )
                and (max(differences)) <= 3
            ):
                safe += 1
                break


print(safe)
