with open("2024\Day5\input.txt") as input:
    puzzleinput = input.read().split("\n")
    order_rules = puzzleinput[: puzzleinput.index("")]
    updates = puzzleinput[puzzleinput.index("") + 1 :]

total = 0
temp_update = []


def check_correct(update):
    correct = True
    temp_order_rules = list(set([j for j in order_rules for i in update if i in j]))
    for rule in temp_order_rules:
        rule = rule.split("|")
        try:
            if update.index(rule[0]) > update.index(rule[1]):
                return False

        except Exception as e:
            continue
    if correct:
        return True
    return False


for update in updates:
    update = update.split(",")
    # correct = True
    temp_update = update.copy()

    temp_order_rules = list(set([j for j in order_rules for i in update if i in j]))
    while not check_correct(temp_update):
        for rule in temp_order_rules:
            rule = rule.split("|")
            try:
                if temp_update.index(rule[0]) > temp_update.index(rule[1]):
                    temp_update.remove(rule[0])
                    temp_update.insert(max(temp_update.index(rule[1]) - 1, 0), rule[0])
            except Exception as e:
                continue
    if temp_update != update:
        total += int(temp_update[len(temp_update) // 2])


print(total)
