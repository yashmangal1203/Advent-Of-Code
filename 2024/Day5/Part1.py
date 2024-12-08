with open("2024\Day5\input.txt") as input:
    puzzleinput = input.read().split("\n")
    order_rules = puzzleinput[: puzzleinput.index("")]
    updates = puzzleinput[puzzleinput.index("") + 1 :]

total = 0

for update in updates:
    update = update.split(",")
    correct = True
    for i in update:
        temp_order_rules = [j for j in order_rules if i in j]
        for rule in temp_order_rules:
            rule = rule.split("|")
            try:
                if rule.index(i) == 0 and not (update.index(i) < update.index(rule[1])):
                    correct = False
                elif rule.index(i) == 1 and not (
                    update.index(i) > update.index(rule[0])
                ):
                    correct = False
            except Exception as e:
                # print(e)
                continue
    if correct:
        total += int(update[len(update) // 2])

print(total)
