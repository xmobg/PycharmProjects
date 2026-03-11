guest_list = input().split("|")
while True:
    command = input()
    if command == "PartyTime!":
        break
    parts = command.split()
    action = parts[0]
    name = parts[1]
    if action == "Invite":
        if name not in guest_list:
            guest_list.append(name)
    elif action == "Cancel":
        if name in guest_list:
            guest_list.remove(name)
    elif action == "VIP":
        if name not in guest_list:
            guest_list.insert(0,name)
    elif action == "Swap":
        name1 = parts[1]
        name2 = parts[2]
        if name1 in guest_list and name2 in guest_list:
            index1 = guest_list.index(name1)
            index2 = guest_list.index(name2)
            guest_list[index1] , guest_list[index2] = guest_list[index2], guest_list[index1]
print(", ".join(guest_list))