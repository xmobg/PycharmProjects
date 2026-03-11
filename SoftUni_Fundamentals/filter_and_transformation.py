numbers = list(map(int,input().split()))
numbers = list(dict.fromkeys(numbers))
numbers = [number for number in numbers if number > 0 ]
numbers = sorted([i ** 2 for i in numbers])
print(numbers)
