with open("2016\Day4\input.txt") as input:
    puzzleinput = input.read()
    puzzleinput = puzzleinput.split("\n")

# test_input = """aaaaa-bbb-z-y-x-123[abxyz]
# a-b-c-d-e-f-g-h-987[abcde]
# not-a-real-room-404[oarel]
# totally-real-room-200[decoy]"""

sector_code_sum = 0
correct_rooms = []
for line in puzzleinput:
    words = "".join(line.split("-")[:-1])
    sector_code = line.split("-")[-1].split("[")[0]
    checksum = line.split("-")[-1].split("[")[1].strip("]")
    countdict = {}
    for char in words:
        countdict.setdefault(char, 0)
        countdict[char] += 1

    sorted_dict = sorted(countdict.items(), key=lambda x: (-x[1], x[0]))
    check_sum = ""
    for value in sorted_dict[:5]:
        check_sum += value[0]
    if check_sum == checksum:
        sector_code_sum += int(sector_code)
        correct_rooms.append(line)


def caesar(char, shift):
    if char == "-":
        return " "
    return chr(((ord(char) - 97) + shift) % 26 + 97)


for room in correct_rooms:
    words = "".join(room.split("-")[:-1])
    sector_code = room.split("-")[-1].split("[")[0]
    checksum = room.split("-")[-1].split("[")[1].strip("]")
    new_string = ""
    for char in words:
        new_char = caesar(char, int(sector_code))
        new_string += str(new_char)
    if new_string == "northpoleobjectstorage":
        print(new_string, sector_code)
