morning_tasks = input().split("|")

while True:
    command = input()
    if command == "Finish":
        break

    parts = command.split()
    action = parts[0]

    if action == "AddTask":
        task = parts[1]
        if task not in morning_tasks:
            morning_tasks.append(task)

    elif action == "InsertTask":
        task = parts[1]
        index = int(parts[2])
        if task not in morning_tasks:
            if 0 <= index <= len(morning_tasks):
                morning_tasks.insert(index, task)

    elif action == "RemoveTask":
        task = parts[1]
        if task in morning_tasks:
            morning_tasks.remove(task)

    elif action == "SwapTasks":
        task1 = parts[1]
        task2 = parts[2]
        if task1 in morning_tasks and task2 in morning_tasks:
            idx1 = morning_tasks.index(task1)
            idx2 = morning_tasks.index(task2)
            morning_tasks[idx1], morning_tasks[idx2] = morning_tasks[idx2], morning_tasks[idx1]

print(" | ".join(morning_tasks))
