list_of_numbers = list(map(int, input().split()))
only_even_numbers = []
def even_or_odd(numbers):
    for numbers in list_of_numbers:
        if numbers % 2 == 0:
            only_even_numbers.append(numbers)
even_or_odd(list_of_numbers)
print(only_even_numbers)

