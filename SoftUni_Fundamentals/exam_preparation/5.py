number = list(map(int,input().split()))

print(f"Sum: {sum(number)}")
min_number = number[0]
max_number = number[0]

for number in number:
    if number < min_number:
        min_number = number
    elif number > max_number:
        max_number = number

print(f"Min:{min_number}")
print(f"Max:{max_number}")