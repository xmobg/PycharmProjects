shopping_list = input().split("|")
while True:
    command = input()
    if command == "Done!":
        break

    parts = command.split()
    action = parts[0]
    item = parts[1]
    if action == "Add":
        if item not in shopping_list:
            shopping_list.append(item)
    elif action == "Remove":
        if item in shopping_list:
            shopping_list.remove(item)
    elif action == "Urgent":
        if item not in shopping_list:
            shopping_list.insert(0, item)
print(", ".join(shopping_list))