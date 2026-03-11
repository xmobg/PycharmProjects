gifts = input().split()
while True:
    command = input()
    if command == "No Money":
        break
    parts = command.split()
    gift = parts[1]
    for i in range(len(gifts)):
        if gifts[i] == gift:
            gifts[i] = "None"
    index = int(parts[2])
    if 0 <= index < len(gifts):
        gifts[index] = gift
    