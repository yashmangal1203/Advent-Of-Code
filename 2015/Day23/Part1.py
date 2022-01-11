with open("2015\\Day23\\input.txt") as input:
    puzzleinput = input.read()
    puzzleinput = puzzleinput.split("\n")


instructions = [line for line in puzzleinput]
registers = {"a": 0, "b": 0}
procounter = 0

while True:
    if procounter not in range(len(instructions)):
        break
    line = instructions[procounter]
    inst, r = line.split(" ",1)
    offsetno = 1
    if inst == "hlf":
        registers[r] //= 2
    elif inst == "tpl":
        registers[r] *= 3
    elif inst == "inc":
        registers[r] += 1
    elif inst == "jmp":
        offsetno = int(r)
    elif inst == "jie":
        r, offset = r.split(",")
        if registers[r] % 2 == 0:
            offsetno = int(offset)
    elif inst == "jio":
        r, offset = r.split(",")
        if registers[r] == 1:
            offsetno = int(offset)
    else:
        raise ValueError(line)
    procounter += offsetno
print(registers["b"])
