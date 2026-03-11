text = input()

while True:
    command = input()
    if command == "Reveal":
        break
    parts = command.split(":")

    if parts[0] == "InsertSpace":
        index = int(parts[1])
        text = text[:index] + " " + text[index:]
        print(text)

    elif parts[0] == "Reverse":
        substring = parts[1]
        if substring in text:
            text = text.replace(substring, "", 1)
            text += substring[::-1]
            print(text)
        else:
            print("error")

    elif parts[0] == "ChangeAll":
        substring = parts[1]
        replacement = parts[2]
        text = text.replace(substring, replacement)
        print(text)

print(f"You have a new text message: {text}")