numbers = list(map(int,input().split()))
numbers = list(dict.fromkeys(numbers))
numbers = sorted([number for number in numbers if 99 > number > 10 and number % 3 == 0 ],reverse=True)
print(numbers)

