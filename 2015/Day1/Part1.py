with open('2015\Day1\input.txt') as input:
    puzzleinput = input.read()

upcount = puzzleinput.count('(')
downcount = puzzleinput.count(')')
level = 0 + upcount - downcount

print('Santa is at level: ', level)  # 74
