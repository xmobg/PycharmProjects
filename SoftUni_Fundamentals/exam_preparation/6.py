numbers = list(map(int,input().split()))
while True:
    parts = input()
    if parts == "end":
        break

    parts = parts.split()
    command = parts[0]
    if command == "Add":
        number = int(parts[1])
        numbers.append(number)
    elif command == "Remove":
        number = int(parts[1])
        numbers.remove(number)
    elif command == "RemoveAt":
        number = int(parts[1])
        numbers.pop(number)
    elif command == "Insert":
        number = int(parts[1])
        index = int(parts[2])
        numbers.insert(index, number)
print(" ".join(map(str,numbers)))