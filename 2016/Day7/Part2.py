with open("2016\Day7\input.txt") as input:
    puzzleinput = input.read()
    puzzleinput = puzzleinput.split("\n")


def check_SSL(hypernetseq, ip):
    for seq in hypernetseq:
        for i in range(len(seq) - 2):
            if seq[i] == seq[i + 2]:
                word = seq[i : i + 3]
                newword = word[1] + word[0] + word[1]
                for j in ip:
                    if newword in j:
                        return True
    return False


ssl = 0
for line in puzzleinput:
    line += "["
    ips = []
    hypernet_seq = []
    ip = ""
    hypernet_sequence = ""
    hypernet = False
    for char in line:  
        if char == "[":
            hypernet = True
            ips.append(ip)
            ip = ""
            continue
        elif char == "]":
            hypernet = False
            hypernet_seq.append(hypernet_sequence)
            hypernet_sequence = ""
            continue
        if hypernet:
            hypernet_sequence += char
        else:
            ip += char
    if check_SSL(hypernet_seq, ips):
        ssl += 1

print(ssl)
