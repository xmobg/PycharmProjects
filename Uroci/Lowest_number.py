"""
The user enters three numbers. Find and print the smallest one.
"""

number_one = int(input("Enter the first number: "))
number_two = int(input("Enter the second number: "))
number_three = int(input("Enter the third number: "))

if number_one < number_two and number_one < number_three:
    lowest_number = number_one
    print("The smallest number is ", lowest_number)
elif number_two < number_one and number_two < number_three:
    lowest_number = number_two
    print("The smallest number is ", lowest_number)
else:
    lowest_number = number_three
    print("The smallest number is ", lowest_number)