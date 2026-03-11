energy = int(input())
round_won = 0
while True:
    distance = input()
    if distance == "End of battle":
        print(f"Won battles: {round_won}. Energy left: {energy}")
        break
    distance = int(distance)
    if energy < distance:
        print(f"Not enough energy! Game ends with {round_won} won battles and {energy} energy")
        break
    energy -= distance
    round_won += 1
    if round_won % 3 == 0:
        energy += round_won