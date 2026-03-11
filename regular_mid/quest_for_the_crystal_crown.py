energy = float(input())
water = int(input())
supplies = int(input())
artefact = 0
artefact_count = 0
while True:
    action = input()
    if action == "Expedition ends":
        break
    elif action == "mountain":
        energy -= 12
        artefact_count += 1
        if artefact_count % 4 == 0:
            artefact += 1
    elif action == "desert":
        energy -= 15
        water -= 5
    elif action == "forest":
        energy += 7
        supplies += 3
    elif action == "river":
        energy -= 5
        water -= 8
    elif action == "village":
        water += 10
        supplies += 5
    elif action == "cave":
        energy -= 10
        supplies -= 2
    elif action == "crystal" and artefact_count > 0:
        artefact += 1
    if energy <= 0 or water <= 0 or supplies <= 0:
        print("The hero couldn't continue the quest.")
        break
    if artefact == 4:
        print(f"The hero found the Crystal Crown with {energy:.2f} energy, {water} water, and {supplies} supplies left.")
        break
print(f"The hero stopped searching. He needed {4-artefact} more pieces to complete the Crystal Crown.")

