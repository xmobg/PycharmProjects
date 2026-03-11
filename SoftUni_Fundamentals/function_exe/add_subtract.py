def sum_numbers(first_number : int, second_number:int):
    return first_number + second_number
def substract(result : int , third_number:int):
    return result - third_number

def sum_substract(first_number : int, second_number : int, third_number : int):
    result = sum_numbers(first_number, second_number)
    final_result = substract(result, third_number)
    return final_result

first_int = int(input())
second_int = int(input())
third_int = int(input())
print(sum_substract(first_int, second_int, third_int))
