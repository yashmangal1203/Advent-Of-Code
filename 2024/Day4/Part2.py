with open("2024\Day4\input.txt") as input:
    puzzleinput = input.read().split("\n")

grid = [list(word) for word in puzzleinput]

found = 0
all_found = [[""], [""]]

for row_index, row in enumerate(grid):
    for col_index, col in enumerate(row):
        try:
            if col == "A":
                all_found[0] = (
                    grid[row_index - 1][col_index - 1]
                    + "A"
                    + grid[row_index + 1][col_index + 1]
                )
                all_found[1] = (
                    grid[row_index - 1][col_index + 1]
                    + "A"
                    + grid[row_index + 1][col_index - 1]
                )
                if all_found.count("MAS") + all_found.count("SAM") == 2:
                    found += 1
        except IndexError:
            continue
print(found)
