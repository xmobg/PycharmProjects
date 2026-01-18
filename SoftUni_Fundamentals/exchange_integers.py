number_one = int(input())
number_two = int(input())
number_three = 0
print(f"Before: \n a = {number_one} \n b = {number_two}")
number_three = number_one
number_one = number_two
number_two = number_three
print(f"After: \n a = {number_one} \n b = {number_two}")