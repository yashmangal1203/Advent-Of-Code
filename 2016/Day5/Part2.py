with open("2016\Day5\input.txt") as input:
    puzzleinput = input.read()

import hashlib
import itertools as it

code = [0, 0, 0, 0, 0, 0, 0, 0]
lastnum = 1

c = []
while len(c) < 8:
    for j in it.count(lastnum + 1):
        newstr = puzzleinput
        newstr += str(j)
        hash_obj = hashlib.md5(newstr.encode())
        if str(hash_obj.hexdigest()).startswith("00000"):
            try:
                if 0 <= int(str(hash_obj.hexdigest())[5]) <= 7:
                    position = int(str(hash_obj.hexdigest())[5])
                    if position not in c:
                        code[position] = str(hash_obj.hexdigest())[6]
                        lastnum = j
                        print(lastnum)
                        c.append(position)
                        break
            except:
                continue

print(code)
