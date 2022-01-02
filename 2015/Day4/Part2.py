#! This is a very brute force method and I wouldn't recommend this. But I had no idea what  MD5 hashes was so I went with this. Took a while but got the answer.

import hashlib

with open("2015\Day4\input.txt") as input:
    puzzleinput = input.read()

Found = False
number = 1
while not Found:
    hash_string = puzzleinput + str(number)
    hash_obj = hashlib.md5(hash_string.encode())
    print(hash_string)
    if hash_obj.hexdigest()[0:6] == "000000":
        Found = True
        break
    else:
        number += 1
        continue

print(hash_string)  # iwrupvqb9958218
