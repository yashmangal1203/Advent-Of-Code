with open("2015\\Day19\\input.txt") as input:
    puzzleinput = input.read()
    puzzleinput = puzzleinput.split("\n")


replacements = [i for i in puzzleinput[:-2]]
molecule = puzzleinput[-1]
possibilities = set()
for replacement in replacements:
    replacement = replacement.split(" => ")
    old = replacement[0]
    new = replacement[1]
    lastfound = None
    for i in range(len(molecule)):
        if molecule[i : i + len(old)] == old:
            newstring = molecule[:i] + new + molecule[i + len(old) :]
            possibilities.add(newstring)

print(len(possibilities))
