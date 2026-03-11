def process_command(cmd,fuel,data_point,obstacle_count):
    if cmd == "move":
        fuel -= 10
    elif cmd == "scan":
        fuel -= 5
    elif cmd == "charge":
        fuel += 15
    elif cmd == "obstacle":
        fuel -= 20
        obstacle_count += 1
        if obstacle_count % 3 == 0:
            data_point += 1
    return fuel,data_point, obstacle_count

fuel = float(input())
data_point = 0
obstacle_count = 0

while True:
    cmd = input()
    if cmd == "Shutdown":
        if data_point >= 3:
            print(f"Exploration complete! Energy left: {int(fuel)}")
            break
        else:
            print(f"Incomplete mission. Need {3 - data_point} more data.")
            break
    fuel, data_point, obstacle_count = process_command(cmd, fuel, data_point, obstacle_count)
    if fuel <= 0 :
        print(f"Robot stopped! Battery depleted.")
        break
    if data_point >= 3:
        print(f"Exploration complete! Energy left: {int(fuel)}")
        break


