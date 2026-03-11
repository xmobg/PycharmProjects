targets = list(map(int, input().split()))

while True:
    command = input()
    if command == "End":
        break

    parts = command.split()
    action = parts[0]

    if action == "Shoot":
        index = int(parts[1])
        power = int(parts[2])
        if 0 <= index < len(targets):
            targets[index] -= power
            if targets[index] <= 0:
                targets.pop(index)

    elif action == "Add":
        index = int(parts[1])
        value = int(parts[2])
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        index = int(parts[1])
        radius = int(parts[2])
        left = index - radius
        right = index + radius
        if left >= 0 and right < len(targets):
            for i in range(right, left - 1, -1):
                targets.pop(i)
        else:
            print("Strike missed!")

print("|".join(map(str, targets)))
