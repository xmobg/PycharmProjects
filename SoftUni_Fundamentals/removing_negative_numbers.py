numbers = list(map(int, input().split()))
new_numbers = []

for number in numbers:
    if number >= 0:
        new_numbers.append(number)

print(new_numbers)