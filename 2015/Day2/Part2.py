with open('2015\Day2\input.txt') as input:
    puzzleinput = input.read()

giftlist = puzzleinput.split('\n')
totalribbon = 0

for gift in giftlist:
    l, w, h = list(map(int, gift.split('x')))
    dimensions = sorted([l, w, h])
    ribbon = 2*(dimensions[0]+dimensions[1])
    bow = l*w*h
    totalribbon += ribbon + bow

print(totalribbon)  # 3842356
