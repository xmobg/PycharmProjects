numbers = list(map(int, input().split()))
number_to_remove = int(input())

for _ in range(number_to_remove):
    smallest_number = min(numbers)
    numbers.remove(smallest_number)

print(", ".join(map(str, numbers)))