def calculate_factorial(some_number: int) -> int:
    for current_number in range(1,some_number):
        some_number *= current_number
    return some_number
first_int = int(input())
second_int = int(input())
first_factorial  = calculate_factorial(first_int)
second_factorial = calculate_factorial(second_int)
result = first_factorial / second_factorial
print(f"{result:.2f}")