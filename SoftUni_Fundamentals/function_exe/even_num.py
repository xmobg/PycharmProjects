def even_num(num:int)->bool:
    return num % 2 == 0


numbers_as_str = input().split()
numbers_as_dig = []
for digit in numbers_as_str:
    numbers_as_dig.append(int(digit))

result = list(filter(even_num, numbers_as_dig))
print(result)