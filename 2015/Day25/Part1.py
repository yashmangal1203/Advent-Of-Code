r = 20151125
row = 2981
col = 3075

s = sum(range(col + 1))
for a in range(row - 1):
    s += col + a

for a in range(1, s):
    r = r * 252533 % 33554393

print(r)  #! 9132360
