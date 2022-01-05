with open("2015\\Day12\\input.txt") as input:
    puzzleinput = input.read()

sum1 = 0
number = ""

# The way python handles the input.txt is that it treat everychar as a string so its easy to make out numbers/digits and add them!
for i in range(len(puzzleinput)):
    if puzzleinput[i] == "-":
        number += "-"
    elif puzzleinput[i].isdigit():
        number += puzzleinput[i]
    else:
        if number != "":
            sum1 += int(number)
            number = ""
print(sum1)  #! 111754
