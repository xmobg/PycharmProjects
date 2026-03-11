factor_int = int(input())
count_int = int(input())
numbers = []
for multiplier in range(1, count_int + 1):
    numbers.append(multiplier * factor_int)

print(numbers)