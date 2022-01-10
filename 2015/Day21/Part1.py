import itertools as it

boss = {"hitpoints": 109, "damage": 8, "armor": 2}
player = {"hitpoints": 100, "damage": 0, "armor": 0}

weapons = {
    "dagger": {"gold": 8, "damage": 4, "armor": 0},
    "shortsword": {"gold": 10, "damage": 5, "armor": 0},
    "Warhammer": {"gold": 25, "damage": 6, "armor": 0},
    "Longsword": {"gold": 40, "damage": 7, "armor": 0},
    "Greataxe": {"gold": 74, "damage": 8, "armor": 0},
}
armors = {
    "Leather": {"gold": 13, "damage": 0, "armor": 1},
    "Chainmail": {"gold": 31, "damage": 0, "armor": 2},
    "Splintmail": {"gold": 53, "damage": 0, "armor": 3},
    "Bandedmail": {"gold": 75, "damage": 0, "armor": 4},
    "Platemail": {"gold": 102, "damage": 0, "armor": 5},
    " ": {"gold": 0, "damage": 0, "armor": 0},
}
rings = {
    "Damage +1": {"gold": 25, "damage": 1, "armor": 0},
    "Damage +2": {"gold": 50, "damage": 2, "armor": 0},
    "Damage +3": {"gold": 100, "damage": 3, "armor": 0},
    "Defense +1": {"gold": 20, "damage": 0, "armor": 1},
    "Defense +2": {"gold": 40, "damage": 0, "armor": 2},
    "Defense +3": {"gold": 80, "damage": 0, "armor": 3},
    "1": {"gold": 0, "damage": 0, "armor": 0},  # Decoy
    "2": {"gold": 0, "damage": 0, "armor": 0},  # Decoy
}


def did_Player_Win(phealth, bhealth, pattack, battack):
    while bhealth > 0:
        bhealth -= pattack
        phealth -= battack
    if phealth > 0:
        return True
    else:
        return False


gold = []

# You could use it.product as well reduces the 3 nested loopt to 1 loop!
for weapon in weapons.keys():
    for armor in armors.keys():
        for perm in it.combinations(rings.keys(), 2):
            player["armor"] = armors[armor]["armor"] + rings[perm[0]]["armor"] + rings[perm[1]]["armor"]
            player["damage"] = weapons[weapon]["damage"] + rings[perm[0]]["damage"] + rings[perm[1]]["damage"]
            bossattack = boss["damage"] - player["armor"]
            playerattack = player["damage"] - boss["armor"]
            if did_Player_Win(player["hitpoints"], boss["hitpoints"], playerattack, bossattack):
                gold.append(
                    armors[armor]["gold"] + rings[perm[0]]["gold"] + rings[perm[1]]["gold"] + weapons[weapon]["gold"]
                )

print(min(gold))
