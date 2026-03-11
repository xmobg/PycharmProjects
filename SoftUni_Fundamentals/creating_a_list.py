lines = int(input())
number = []
for _ in range(lines):
    number_to_list = int(input())
    number.append(number_to_list)

print(sum(number))