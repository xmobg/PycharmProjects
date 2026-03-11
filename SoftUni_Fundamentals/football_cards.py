gifts = input().split()
command = input()

while command != 'End':
    parts = command.split()
    action = parts[0]

    if action == 'Remove':
        gift = parts[1]
        for i in range(len(gifts)):
            if gifts[i] == gift:
                gifts[i] = "Empty"

    elif action == "Swap":
        gift = parts[1]
        index = int(parts[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift

    elif action == "Surprise":
        gift = parts[1]
        gifts.insert(0, gift)

    command = input()

print(" ".join([g for g in gifts if g != "Empty"]))
