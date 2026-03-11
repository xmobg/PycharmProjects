groceries_list = input().split("!")
command = input()

while command != "Go Shopping!":
    parts = command.split()
    action = parts[0]
    name = parts[1]

    if action == "Urgent":
        if name not in groceries_list:
            groceries_list.insert(0, name)

    elif action == "Unnecessary":
        if name in groceries_list:
            groceries_list.remove(name)

    elif action == "Correct":
        new_name = parts[2]
        if name in groceries_list:
            index = groceries_list.index(name)
            groceries_list[index] = new_name

    elif action == "Rearrange":
        if name in groceries_list:
            groceries_list.remove(name)
            groceries_list.append(name)

    command = input()

print(", ".join(groceries_list))
