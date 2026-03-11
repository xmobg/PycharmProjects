numbers = [10, 15, 20, 25, 30, 35, 40]
numbers_devide = list(filter(lambda x: x % 20 == 0, numbers))
print(numbers_devide)