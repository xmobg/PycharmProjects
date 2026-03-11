
numbers = []

for number in range(11):
    numbers.append(number)

searching_numbers = int(input())
if searching_numbers in numbers:
    print("YES")
else:
    print("NO")
