def process_command(cmd,fuel,astroids,maps):
    if cmd == "nebula":
        fuel -= 20.5
    elif cmd == "asteroid-field":
        fuel -= 15
        astroids += 1
        if astroids % 2 == 0:
            maps += 1
    elif cmd == "space-station":
        fuel += 10
    return fuel,astroids,maps


fuel = float(input())
maps = 0
astroids = 0

while True:
    cmd = input()

    if cmd == "Mission Accomplished":
        if maps >= 4:
            print(f"Mission successful! Remaining fuel: {fuel:.2f}.")
        else:
            print(f"Not enough maps. Need {4 - maps} more.")
        break

    fuel,astroids,maps = process_command(cmd,fuel,astroids,maps)

    if fuel <= 0:
        print("Mission failed! Out of fuel.")
        break

    if maps == 4:
        print(f"Mission successful! Remaining fuel: {fuel:.2f}.")
        break
