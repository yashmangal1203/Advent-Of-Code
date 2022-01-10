import re

with open("2015\\Day19\\input.txt") as input:
    puzzleinput = input.read()

# This one was entirely copied from reddit comments. There is a very nice explanation to this answer as well.
# Link - https://www.reddit.com/r/adventofcode/comments/3xflz8/comment/cy4nsdd/?utm_source=share&utm_medium=web2x&context=3
molecule = puzzleinput.split("\n")[-1][::-1]
reps = {m[1][::-1]: m[0][::-1] for m in re.findall(r"(\w+) => (\w+)", puzzleinput)}


def rep(x):
    return reps[x.group()]


count = 0
while molecule != "e":
    molecule = re.sub("|".join(reps.keys()), rep, molecule, 1)
    count += 1

print(count)
