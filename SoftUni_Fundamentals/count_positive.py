numbers = list(map(int, input().split()))
count = 0
for number in numbers:
    if number > 0:
        count += 1

print(count)