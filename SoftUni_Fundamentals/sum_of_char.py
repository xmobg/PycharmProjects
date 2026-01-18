numbers_of_line = int(input())
total_sum = 0

for i in range(numbers_of_line):
    i = ord(input())
    total_sum += i
print(f"The sum equals: {total_sum}")