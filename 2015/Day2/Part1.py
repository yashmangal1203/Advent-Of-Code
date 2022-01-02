with open('2015\Day2\input.txt') as input:
    puzzleinput = input.read()

giftlist = puzzleinput.split('\n')
totalpaper = 0

for gift in giftlist:
    l, w, h = list(map(int, gift.split('x')))
    dimension = sorted([l, w, h])
    surfacearea = (2*l*w) + (2*w*h) + (2*h*l)
    slack = dimension[0]*dimension[1]
    totalpaper += surfacearea + slack

print(totalpaper)  # 1606483
