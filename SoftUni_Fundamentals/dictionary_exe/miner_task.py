resourse = {}
current_resourse = input()

while current_resourse != "stop":
    current_quantity = int(input())
    if current_resourse not in resourse.keys():
        resourse[current_resourse] = 0
    resourse[current_resourse] += current_quantity
    current_resourse = input()
for resourse,quantity in resourse.items():
    print(f"{resourse} -> {quantity}")