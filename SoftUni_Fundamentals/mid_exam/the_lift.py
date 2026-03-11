people_for_lift = int(input())
wagons = list(map(int, input().split()))
for i in range(len(wagons)):
    free_space = 4 - wagons[i]
    if people_for_lift <= 0 :
        break
    if free_space > 0:
        to_get_in = min(people_for_lift,free_space)
        wagons[i] += to_get_in
        people_for_lift -= to_get_in
if people_for_lift > 0:
    print(f"There isn't enough space! {people_for_lift} people in a queue!")
    print(" ".join(map(str, wagons)))
elif any(w < 4 for w in wagons):
    print("The lift has empty spots!")
    print(" ".join(map(str, wagons)))
else:
    print(" ".join(map(str, wagons)))
