numbers = list(map(int, input().split()))
new_list = []
print(numbers)
print(numbers[::-1])
for number in reversed(numbers):
    new_list.append(number)

print(new_list)
