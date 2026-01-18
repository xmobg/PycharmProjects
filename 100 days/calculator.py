number_one = float(input("Please enter a number: "))
operator = input("Please enter your operator: ")

if operator == "+":
    number_two = float(input("Please enter another number: "))
    sum = number_one + number_two
    print(f"The sum is: {sum:.2f}")
elif operator == "-":
    number_two = float(input("Please enter another number: "))
    sum = number_one - number_two
    print(f"The sum is: {sum:.2f}")
elif operator == "*":
    number_two = float(input("Please enter another number: "))
    sum = number_one * number_two
    print(f"The sum is: {sum:.2f}")
elif operator == "/":
    number_two = float(input("Please enter another number: "))
    sum = number_one / number_two
    print(f"The sum is: {sum:.2f}")
else:
    print("Please enter a valid operator")
