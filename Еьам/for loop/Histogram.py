count = int(input())

count_p1 = 0
count_p2 = 0
count_p3 = 0
count_p4 = 0
count_p5 = 0
for _ in range(count):
    current_num = int(input())

    if current_num < 200:
        count_p1 += 1
    elif 200 <= current_num <= 399 :
        count_p2 += 1
    elif 400<= current_num <= 599 :
        count_p3 += 1
    elif 600 <= current_num <= 799 :
        count_p4 += 1
    else:
        count_p5 += 1

percentage_p1 = count_p1 / count * 100
percentage_p2 = count_p2 / count * 100
percentage_p3 = count_p3 / count * 100
percentage_p4 = count_p4 / count * 100
percentage_p5 = count_p5 / count * 100

print(f"{percentage_p1:.2f}%")
print(f"{percentage_p2:.2f}%")
print(f"{percentage_p3:.2f}%")
print(f"{percentage_p4:.2f}%")
print(f"{percentage_p5:.2f}%")


