nums = [3, 5, 10, 12, 15, 20, 25, 30]
numbers = list(filter(lambda x: x% 5 == 0, nums))
numbers = list(map(lambda x: x * 2, numbers))
numbers = [f"{num} е ново число" for num in numbers  ]
print(numbers)