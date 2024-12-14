from pprint import pprint

with open("2024\Day6\input.txt") as input:
    puzzleinput = input.read().split("\n")
    puzzleinput = [list(i) for i in puzzleinput]

puzzleinput.insert(0, ["X"] * len(puzzleinput[0]))
puzzleinput.append(["X"] * len(puzzleinput[0]))
for i in puzzleinput:
    i.insert(0, "X")
    i.append("X")

# print(puzzleinput)

for i, j in enumerate(puzzleinput):
    try:
        col_index, row_index = j.index("^"), i
    except Exception:
        continue

print((row_index, col_index))


def get_next_coords(current_coord, rotation):
    if rotation == "^":
        next_coords = [
            (i, current_coord[1]) for i in range(current_coord[0] - 1, -1, -1)
        ]
    elif rotation == ">":
        next_coords = [
            (current_coord[0], i) for i in range(current_coord[1], len(puzzleinput[1]))
        ]
    elif rotation == "v":
        next_coords = [
            (i + 1, current_coord[1])
            for i in range(current_coord[0], len(puzzleinput[1]))
        ]
    elif rotation == "<":
        next_coords = [
            (current_coord[0], i - 1) for i in range(current_coord[1], -1, -1)
        ]

    return next_coords


next_rotation = {"^": ">", ">": "v", "v": "<", "<": "^"}

found_obs, found_end = False, False

visited = []
last_rotation = "^"

while not found_end:
    found_obs = False
    while not found_obs:
        for i in get_next_coords(
            (row_index, col_index), puzzleinput[row_index][col_index]
        ):
            if puzzleinput[i[0]][i[1]] == "#":
                puzzleinput[row_index][col_index] = next_rotation.get(last_rotation)
                last_rotation = next_rotation.get(last_rotation)
                found_obs = True
                break
            elif puzzleinput[i[0]][i[1]] == "X":
                found_end = True
                found_obs = True
                break
            else:
                row_index, col_index = i[0], i[1]
                visited.append(i)
print(len(set(visited)))
