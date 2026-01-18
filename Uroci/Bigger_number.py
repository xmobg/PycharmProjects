"""
The user enters three numbers. Find and print the biggest one.
"""
number_one = int(input("Enter a number: "))
number_two = int(input("Enter another number: "))
number_three = int(input("Enter another number: "))

if number_one > number_two and number_one > number_three:
    biggest_number = number_one
    print("The biggest number is ", biggest_number)
elif number_two > number_one and number_two > number_three:
    biggest_number = number_two
    print("The biggest number is ", biggest_number)
else:
    biggest_number = number_three
    print("The biggest number is ", biggest_number)
