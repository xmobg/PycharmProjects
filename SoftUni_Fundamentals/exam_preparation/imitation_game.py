text = input()

while True:
    command = input()
    if command == "Decode":
        break
    parts = command.split("|")
    action = parts[0]

    if action == "Move":
        n = int(parts[1])
        text = text[n:] + text[:n]

    elif action == "Insert":
        index = int(parts[1])
        value = parts[2]
        text  = text[:index] + value + text[index:]

    elif action == "ChangeAll":
        substring = parts[1]
        replacement = parts[2]
        text = text.replace(substring, replacement)

print(f"The decrypted message is: {text}")


