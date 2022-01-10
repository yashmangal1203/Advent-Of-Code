with open("2015\\Day20\\input.txt") as input:
    puzzleinput = input.read()

from math import sqrt

factors = set()
houseno = 1
totalgifts = 0

while totalgifts < 34000000:
    for i in range(1, int(sqrt(houseno) + 1)):
        div, mod = divmod(houseno, i)
        if mod == 0:
            factors.add(i)
            factors.add(div)
    totalgifts = 10 * (sum(factors))
    factors = set()
    houseno += 1

print(houseno - 1) #! 786240
