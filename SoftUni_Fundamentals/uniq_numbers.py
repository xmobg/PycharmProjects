numbers = list(map(int,input().split()))
numbers = list(dict.fromkeys(numbers))
even_number = sorted([x for x in numbers if x % 2 == 0])
print(even_number)