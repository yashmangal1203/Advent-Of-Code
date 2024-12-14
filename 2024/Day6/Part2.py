# This is no way the best solution, but I bruteforced and got a correct answer. Which works for me.

from copy import deepcopy

with open("2024\Day6\input.txt") as input:
    puzzleinput = input.read().split("\n")
    puzzleinput = [list(i) for i in puzzleinput]

puzzleinput.insert(0, ["X"] * len(puzzleinput[0]))
puzzleinput.append(["X"] * len(puzzleinput[0]))
for i in puzzleinput:
    i.insert(0, "X")
    i.append("X")


for i, j in enumerate(puzzleinput):
    try:
        og_col_index, og_row_index = j.index("^"), i
    except Exception:
        continue


def get_next_coords(current_coord, rotation):
    if rotation == "^":
        next_coords = [
            (i, current_coord[1]) for i in range(current_coord[0] - 1, -1, -1)
        ]
    elif rotation == ">":
        next_coords = [
            (current_coord[0], i)
            for i in range(current_coord[1] + 1, len(puzzleinput[1]))
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


def ended(puzzleinput, temp_row_index, temp_col_index):
    visited = {}
    last_rotation = "^"
    found_obs, found_end, looping = False, False, 0
    list_nextcoords = []
    while not found_end and looping < 3:
        found_obs = False

        while not found_obs:
            next_coords = get_next_coords(
                (temp_row_index, temp_col_index),
                puzzleinput[temp_row_index][temp_col_index],
            )
            if next_coords in list_nextcoords:
                looping += 1
            else:
                list_nextcoords.append(next_coords)

            for i in next_coords:
                if puzzleinput[i[0]][i[1]] == "#":
                    puzzleinput[temp_row_index][temp_col_index] = next_rotation.get(
                        last_rotation
                    )
                    last_rotation = next_rotation.get(last_rotation)
                    found_obs = True
                    break
                elif puzzleinput[i[0]][i[1]] == "X":
                    found_end = True
                    found_obs = True
                    break
                else:
                    puzzleinput[temp_row_index][temp_col_index] = "."
                    temp_row_index, temp_col_index = i[0], i[1]
                    visited[i] = last_rotation
    return False if looping < 3 else True


current_coord = (og_row_index, og_col_index)
next_coords = get_next_coords(
    (og_row_index, og_col_index), puzzleinput[og_row_index][og_col_index]
)

found_obs, found_end = False, False
last_rotation = "^"
found_looper = []
row_index, col_index = og_row_index, og_col_index
while not found_end:
    found_obs = False
    while not found_obs:
        next_coords = get_next_coords((row_index, col_index), last_rotation)
        for j, i in enumerate(next_coords):
            if puzzleinput[i[0]][i[1]] == "#":
                last_rotation = next_rotation.get(last_rotation)
                found_obs = True

                break
            elif puzzleinput[i[0]][i[1]] == "X":
                found_end = True
                found_obs = True
                break

            else:
                temp_puzzleinput = deepcopy(puzzleinput)
                if not (next_coords[j][0], next_coords[j][1]) == (80, 88):
                    temp_puzzleinput[next_coords[j][0]][next_coords[j][1]] = "#"
                else:
                    continue
                if ended(temp_puzzleinput, og_row_index, og_col_index):
                    found_looper.append((next_coords[j][0], next_coords[j][1]))
                row_index, col_index = i[0], i[1]


print(len(list(set(found_looper))))
