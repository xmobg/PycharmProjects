numbers_of_room = int(input())
total_free_chairs = 0
for numbers_of_room in range(1, numbers_of_room + 1):
    chairs_in_current_room, visitors = input().split()
    difference = len(chairs_in_current_room) - int(visitors)
    if difference < 0:
        print(f"{abs(difference)} more chairs needed in room {numbers_of_room}")
    total_free_chairs += difference
if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")