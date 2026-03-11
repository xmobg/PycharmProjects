# Move zeros to the end (keep order of non-zeros) but do it in place without a new list.
# Hint: you can use two pointers that go over the indexes of the array
my_list = [0, 1, 0, 3, 12]

non_zero_num = 0

for element in range(len(my_list)):
    if my_list[element] != 0:
        my_list[non_zero_num] , my_list[element] = my_list[element] , my_list[non_zero_num]
        non_zero_num += 1
print(my_list)
