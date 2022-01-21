with open("2016\Day7\input.txt") as input:
    puzzleinput = input.read()
    puzzleinput = puzzleinput.split("\n")


def check_ABBA(hypernetseq, ip):
    for seq in hypernetseq:
        for i in range(len(seq) - 3):
            if seq[i] != seq[i + 1]:
                if seq[i] == seq[i + 3]:
                    if seq[i + 1] == seq[i + 2]:
                        return False
    for ip in ips:
        for i in range(len(ip) - 3):
            if ip[i] != ip[i + 1]:
                if ip[i] == ip[i + 3]:
                    if ip[i + 1] == ip[i + 2]:
                        return True


tls = 0
for line in puzzleinput:
    line += "["
    ips = []
    hypernet_seq = []
    ip = ""
    hypernet_sequence = ""
    hypernet = False
    for char in line:  # "ioxxoj[asdfgh]zxcvbn"
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
    if check_ABBA(hypernet_seq, ips):
        print(hypernet_seq)
        tls += 1

print(tls)
