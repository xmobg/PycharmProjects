def positive_num(nums):
    return [n for n in nums if n > 0 ]

list_of_elements = [-2, 5, 0, 3, -1]
print(positive_num(list_of_elements))
double_num = [1,2,3]
def power_num(nums):
    return [n*2  for n in nums if n > 0 ]
print(power_num(double_num))
list_of_integers = [1,2,3,4,5,6,7,8,9,10]
def max_in_list(nums):
    max_num = nums[0]
    for n in nums:
        if n > max_num:
            max_num = n
    return max_num
print(max_in_list(list_of_integers))