with open("2015\\Day10\\input.txt") as input:
    puzzleinput = input.read()
    puzzleinput


def look_and_say(s):
    last = s[0]
    count = 1
    news = ""
    for number in s[1:]:
        if number == last:
            count += 1
        else:
            news += str(count) + last
            last = number
            count = 1
    return news + str(count) + last


# Fortunatly the way my solution is written the Part 1 and Part 2 only required changing the loop from looping 40 to 50times.
for i in range(50):
    puzzleinput = look_and_say(puzzleinput)

print(len(puzzleinput))  #! 5103798
