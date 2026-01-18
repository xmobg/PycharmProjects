number_of_char = int(input())
total_sum = 0
for char in range(number_of_char):
    current_char = input()
    total_sum += ord(current_char)
print(f"The sum equals: {total_sum}")