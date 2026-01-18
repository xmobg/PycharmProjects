room_size = int(input()) * int(input()) * int(input())
cartons_total = 0
is_enough_space = False
while room_size > cartons_total:
    cartons = input()
    cartons_total += int(cartons)
    if cartons == "Done":
        is_enough_space = True
        break

if is_enough_space:
    print(f"{room_size - cartons_total} Cubic meters left.")
else:
    print(f"No more free space! You need {cartons_total - room_size} Cubic meters more.")






