grid = list(map(int,input().split("|")))
total_item = 0

while True:
    command = input()

    if command == "Hunt Over":
        break

    elif command.startswith("Jump Forward$"):
        _,start,steps = command.split("$")
        start = int(start)
        steps = int(steps)
        if 0<= start < len(grid):
            new_index = (start + steps) % len(grid)
            total_item += grid[new_index]
            grid[new_index] = 0

    elif command.startswith("Jump Backward$"):
        _,start,steps = command.split("$")
        start = int(start)
        steps = int(steps)
        if 0<= start < len(grid):
            new_index = (start - steps) % len(grid)
            total_item += grid[new_index]
            grid[new_index] = 0

    elif command.startswith("Treasure Boost"):
        index = int(command.split()[2])
        if 0<= index < len(grid):
            grid[index] *= 2

    elif command == "Rotate":
        grid.reverse()


print(" - ".join(str(x) for x in grid))
print(f"Robo collected {total_item} treasures!")
