with open("2015\Day18\input.txt") as input:
    puzzleinput = input.read()
    puzzleinput = puzzleinput.split("\n")


import copy

lightgrid = []

templightgrid = [[0 for i in range(100)] for i in range(100)]

for line in puzzleinput:
    subgrid = list(map(lambda x: x.replace("#", "1").replace(".", "0"), line))  # Just to switch '#' to 1 and '.' to 0.
    lightgrid.append(list(map(int, subgrid)))  # Converts the strings to int


def get_value(tempgrid, x, y):
    # Gives the on or off value at this coordinate
    if x < 0 or y < 0:
        return 0
    elif x > 99 or y > 99:
        return 0
    else:
        return tempgrid[x][y]


def process(grid):
    # Actual process
    for i in range(100):
        for j in range(100):
            for k in range(100):
                neighbourlights = [
                    get_value(grid, j - 1, k - 1),  # -1 -1
                    get_value(grid, j, k - 1),  # 0 -1
                    get_value(grid, j + 1, k - 1),  # 1 -1
                    get_value(grid, j - 1, k),  # -1 0
                    get_value(grid, j + 1, k),  # 1 0
                    get_value(grid, j - 1, k + 1),  # -1 1
                    get_value(grid, j, k + 1),  # 0 1
                    get_value(grid, j + 1, k + 1),  # 1 1
                ]
                if grid[j][k] == 1:
                    if sum(neighbourlights) not in [2, 3]:
                        templightgrid[j][k] = 0
                    else:
                        templightgrid[j][k] = 1

                else:
                    if sum(neighbourlights) == 3:
                        templightgrid[j][k] = 1
                    else:
                        templightgrid[j][k] = 0
        # Default setting all corners as ON even if they were switched off
        templightgrid[0][0] = 1
        templightgrid[0][99] = 1
        templightgrid[99][0] = 1
        templightgrid[99][99] = 1
        grid = copy.deepcopy(templightgrid)
    return grid


newgrid = process(lightgrid)

totalOn = sum([subgrid1.count(1) for subgrid1 in newgrid])
print(totalOn)
