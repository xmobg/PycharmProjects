import sys
number_elements = int(input())
max_element = -sys.maxsize
sum_element = 0
for _ in range(number_elements):
    num = int(input())

    if num > max_element:
        max_element = num

    sum_element += num

half_sum = sum_element - max_element

if half_sum == max_element:
    print(f"Yes\nSum = {max_element}")
else:
    print(f"No\nDiff = {abs(half_sum - max_element)}")
