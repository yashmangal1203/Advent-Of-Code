from itertools import count
from math import sqrt

# This was taken from reddit comments. My Solution was simmilar but couldn't get it working fast enough
def factors(n):
    results = set()
    for i in range(1, int(sqrt(n)) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            results.add(i)
            results.add(div)
    return results


def get_n_gifts(number, gifts_per_number=10, limit=None):
    if limit is None:
        n_visits = sum(i for i in factors(number))
    else:
        n_visits = sum(i for i in factors(number) if number <= i * limit)
    return n_visits * gifts_per_number


def get_house_n_gifts(n, gifts_per_number=10, limit=None):
    for i in count(1):
        if get_n_gifts(i, gifts_per_number, limit) >= n:
            return i


def part_two():
    with open("2015\\Day20\\input.txt") as fin:
        puzzle_input = int(fin.read().strip())
    print(get_house_n_gifts(puzzle_input, 11, 50))


if __name__ == "__main__":
    part_two()
