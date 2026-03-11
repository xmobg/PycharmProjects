numbers = list(map(int, input().split(", ")))
even_num = [i for i in range(len(numbers)) if numbers[i] % 2 == 0]
print(even_num)