with open("2015\\Day10\\input.txt") as input:
    puzzleinput = input.read()
    puzzleinput

# ?My solution checks with the previous digit in the number and add in the count until its not same then adds the count and the number to a new string.

# Created a functioin this problem to take the benefit of recursion
def look_and_say(s):
    last_digit = s[0]
    count = 1
    news = ""
    for number in s[1:]:
        if number == last_digit:
            count += 1
        else:
            news += str(count) + last_digit
            last_digit = number
            count = 1
    return news + str(count) + last_digit


# Recursion to repeat the process 40 times.
for i in range(40):
    puzzleinput = look_and_say(puzzleinput)

print(len(puzzleinput))  #! 360154
