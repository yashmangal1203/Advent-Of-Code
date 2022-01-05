# I'm not gonna lie, this isn't my solution. I didn't even a 'JSON' module existed until I checked online for solutions. Sorry.

import json


def day12():
    def sum_numbers(obj):
        if type(obj) == type(dict()):
            if "red" in obj.values():
                return 0
            return sum(map(sum_numbers, obj.values()))

        if type(obj) == type(list()):
            return sum(map(sum_numbers, obj))

        if type(obj) == type(0):
            return obj

        return 0

    data = json.loads(open("2015\\Day12\\input.txt", "r").read())
    return sum_numbers(data)


print(day12())
