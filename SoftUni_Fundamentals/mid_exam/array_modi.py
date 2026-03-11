arr = list(map(int, input().split()))
while True:
    command = input()
    if command == "end":
        break
    parts = command.split()
    action = parts[0]
    if action == "swap":
        index_one = int(parts[1])
        index_two = int(parts[2])
        arr[index_one], arr[index_two] = arr[index_two], arr[index_one]
    if action == "multiply":
        index_one = int(parts[1])
        index_two = int(parts[2])
        arr[index_one] *= arr[index_two]
    if action == "decrease":
        arr = [x - 1 for x in arr]
print(", ".join(map(str, arr)))
