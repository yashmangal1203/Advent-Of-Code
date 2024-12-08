with open("2024\Day4\input.txt") as input:
    puzzleinput = input.read().split("\n")

grid = [list(word) for word in puzzleinput]
search_word = "XMAS"

nearby_letters = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]


def get_straightline(
    first_next_coord, second_next_coord, len_of_searchword, grid_max_rows, grid_max_cols
):
    difference = (
        second_next_coord[0] - first_next_coord[0],
        second_next_coord[1] - first_next_coord[1],
    )
    next_next_coords = []
    next_row_index = 0
    next_col_index = 0
    if difference == (1, 1):
        for i in range(len_of_searchword - 2):
            next_row_index += 1
            next_col_index += 1
            next_next_coords.append((next_row_index, next_col_index))
    elif difference == (1, -1):
        for i in range(len_of_searchword - 2):
            next_row_index += 1
            next_col_index += -1
            next_next_coords.append((next_row_index, next_col_index))
    elif difference == (0, 1):
        for i in range(len_of_searchword - 2):
            next_row_index += 0
            next_col_index += 1
            next_next_coords.append((next_row_index, next_col_index))
    elif difference == (1, 0):
        for i in range(len_of_searchword - 2):
            next_row_index += 1
            next_col_index += 0
            next_next_coords.append((next_row_index, next_col_index))
    elif difference == (0, -1):
        for i in range(len_of_searchword - 2):
            next_row_index += 0
            next_col_index += -1
            next_next_coords.append((next_row_index, next_col_index))
    elif difference == (-1, 1):
        for i in range(len_of_searchword - 2):
            next_row_index += -1
            next_col_index += 1
            next_next_coords.append((next_row_index, next_col_index))
    elif difference == (-1, -1):
        for i in range(len_of_searchword - 2):
            next_row_index += -1
            next_col_index += -1
            next_next_coords.append((next_row_index, next_col_index))
    elif difference == (-1, 0):
        for i in range(len_of_searchword - 2):
            next_row_index += -1
            next_col_index += 0
            next_next_coords.append((next_row_index, next_col_index))
    next_next_coords = [
        (second_next_coord[0] + i[0], second_next_coord[1] + i[1])
        for i in next_next_coords
    ]
    for next in next_next_coords:
        if next[0] >= grid_max_rows or next[1] >= grid_max_cols or next[0] < 0 or next[1] < 0:
            return False
    return next_next_coords

found = 0

for row_index, row in enumerate(grid):
    for col_index, col in enumerate(row):
        if col == search_word[0]:
            # print((row_index, col_index))
            for nearby in nearby_letters:
                if (
                    row_index + nearby[0] < 0
                    or col_index + nearby[1] < 0
                    or row_index + nearby[0] >= len(grid)
                    or col_index + nearby[1] >= len(grid[0])
                ):
                    continue

                if grid[row_index + nearby[0]][col_index + nearby[1]] == search_word[1]:
                    next_coord = get_straightline(
                        (row_index, col_index),
                        (row_index + nearby[0], col_index + nearby[1]),
                        len(search_word),
                        len(grid),
                        len(grid[0]),
                    )
                    if next_coord:
                        if (
                            grid[next_coord[0][0]][next_coord[0][1]] == search_word[2]
                            and grid[next_coord[1][0]][next_coord[1][1]]
                            == search_word[3]
                        ):
                            print(
                                f"coords for all letters {(row_index, col_index),(row_index+nearby[0],col_index+nearby[1]),(next_coord[0][0],next_coord[0][1]),(next_coord[1][0],next_coord[1][1])}"
                            )
                            found += 1

print(found)
