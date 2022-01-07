with open("2015\\Day14\\input.txt") as input:
    puzzleinput = input.read()
    puzzleinput = puzzleinput.split("\n")

names = set()
speeddict = {}
speedtimedict = {}
resttimedict = {}

for word in puzzleinput:
    word = word.split()
    names.add(word[0])  # For names of all elfs
    speeddict[word[0]] = int(word[3])  # For speed of each elf
    speedtimedict[word[0]] = int(word[6])  # For time each elf is awake
    resttimedict[word[0]] = int(word[-2])  # For time each elf is resting


distances = []  # Distance travelled by each elf in the time given.

# ? Goes over each elf and calculates the distance travelled in the given time frame.
for name in names:
    dist = 0
    time = 0
    speed = speeddict[name]
    remain = speedtimedict[name]
    # ? This main loop does the main work.
    while time < 2503:
        dist += speed  # adds the speed every second
        remain -= 1  # reduces the awake time by 1 every second
        if remain == 0:  # when awake time goes 0, this becomes True i.e sleeping time
            if speed:  # if there is speed > 1 while he's resting
                speed = 0  # then speed is made 0 so that dist isn't added
                remain = resttimedict[name]  # Remain becomes the resting time required
            else:
                speed = speeddict[name]
                remain = speedtimedict[name]
        time += 1
    distances.append(dist)

print(max(distances))  #! 2660
