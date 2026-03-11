grid = list(map(int, input().split("|")))
total_item = 0
while True:
    action = input()
    if action == "Adventure over":
        break
    elif action.startswith("Step Backward"):
        parts = action.split("$")
        start = int(parts[1])
        steps = int(parts[2])
        if 0 <= start < len(grid):
            new_index = (start - steps) % len(grid)
            total_item += grid[new_index]
            grid[new_index] = 0
    elif action.startswith("Step Forward"):
        parts = action.split("$")
        start = int(parts[1])
        steps = int(parts[2])
        if 0 <= start < len(grid):
            new_index = (start + steps) % len(grid)
            total_item += grid[new_index]
            grid[new_index] = 0
    elif action.startswith("Double"):
        parts = action.split()
        index = int(parts[1])
        if 0 <= index < len(grid):
            grid[index] *= 2
    elif action == "Switch":
        grid.reverse()
print(" - ".join(map(str, grid)))
print(f"Robo finished the adventure with {total_item} items!")