def average(nums):
    if len(nums) == 0:
        return 0
    return sum(nums) / len(nums)

print(average([2,4,6,8]))
