with open("2015\\Day14\\testinput.txt") as input:
    puzzleinput = input.read()
    puzzleinput = puzzleinput.split("\n")

names = set()
speeds = {}
times1 = {}
rests = {}

for word in puzzleinput:
    word = word.split()
    names.add(word[0])
    speeds[word[0]] = int(word[3])
    times1[word[0]] = int(word[6])
    rests[word[0]] = int(word[-2])


dist = {name: 0 for name in names}
time = 0
states = {name: speeds[name] for name in names}
remains = {name: times1[name] for name in names}
scores = {name: 0 for name in names}
print(dist)
print(states)
print(remains)
print(scores)


while time < 2503:
    for name in names:
        dist[name] += states[name]
        remains[name] -= 1
        if remains[name] == 0:
            if states[name]:
                states[name] = 0
                remains[name] = rests[name]
            else:
                states[name] = speeds[name]
                remains[name] = times1[name]
    time += 1
    winner = [tuple(names)[0]]
    d = dist[winner[0]]
    for name in names:
        if dist[name] > d:
            winner = [name]
            d = dist[name]
        elif dist[name] == d:
            winner.append(name)
    for name in set(winner):
        scores[name] += 1

answer2 = max(scores.values())

print(answer2)
