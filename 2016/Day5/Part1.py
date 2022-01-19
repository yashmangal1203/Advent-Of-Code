with open("2016\Day5\input.txt") as input:
    puzzleinput = input.read()

import hashlib
import itertools as it

code = ""
lastnum = 1
for i in range(8):
    for j in it.count(lastnum+1):
        newstr = puzzleinput
        newstr += str(j)
        hash_obj = hashlib.md5(newstr.encode())
        if str(hash_obj.hexdigest()).startswith("00000"):
            code += str(hash_obj.hexdigest())[5]
            lastnum = j
            print(lastnum)
            break

print(code)
