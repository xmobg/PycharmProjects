numbers = list(map(int, input().split()))
even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)
searching_number = int(input())
if searching_number in numbers:
    print("YES")
else:
    print("NO")