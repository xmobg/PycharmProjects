
input_string = input()
parts = input_string.split("|")
grid = []
for p in parts:
    grid.append(int(p))

total_items = 0


command = input()
while command != "Adventure over":


    if "Step" in command:
        cmd_parts = command.split("$")
        action = cmd_parts[0]
        start_index = int(cmd_parts[1])
        steps = int(cmd_parts[2])


        if start_index >= 0 and start_index < len(grid):
            current_pos = start_index


            for s in range(steps):
                if action == "Step Backward":
                    current_pos -= 1

                    if current_pos < 0:
                        current_pos = len(grid) - 1
                else:
                    current_pos += 1

                    if current_pos >= len(grid):
                        current_pos = 0


            total_items += grid[current_pos]
            grid[current_pos] = 0


    elif "Double" in command:
        cmd_parts = command.split()
        idx = int(cmd_parts[1])
        if idx >= 0 and idx < len(grid):
            grid[idx] = grid[idx] * 2


    elif command == "Switch":

        grid.reverse()

    command = input()


output_grid = ""
for i in range(len(grid)):
    output_grid += str(grid[i])
    if i < len(grid) - 1:
        output_grid += " - "

print(output_grid)
print("Robo finished the adventure with " + str(total_items) + " items!")