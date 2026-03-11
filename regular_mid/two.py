energy = float(input())
water = int(input())
relic = 0
while True:
    action = input()
    if action == "Expedition ends":
        break
    if action == "cave":
        energy -= 12
    elif action == "river":
        energy -= 8
        water -= 5
    elif action == "oasis":
        water += 10
    elif action == "ruins":
        relic += 1
    if energy <= 0 or water <= 0:
        print(f"The explorer couldn't continue the expedition.")
        exit()
    if relic == 5:
        print(f"The explorer found the ancient relic with {energy:.2f} energy and {water} water left.")
        exit()
print(f"The explorer stopped searching. He needed {5 - relic} more pieces.")