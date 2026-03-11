def smallest_number_of_three(list_with_integers: list):
    return min(list_with_integers)

first_int = int(input())
second_int = int(input())
third_int = int(input())
result = smallest_number_of_three([first_int, second_int, third_int])
print(result)
