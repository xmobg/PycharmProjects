def is_perfect_number(number: int) -> str:
    devisors_sum = 0
    for divisor in range(1,number):
        if number % divisor == 0:
            devisors_sum += divisor
    if number == devisors_sum:
        return "We have a perfect number!"
    return "It's not so perfect."

number = int(input())
print(is_perfect_number(number))