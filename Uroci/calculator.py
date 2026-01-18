"""
Write a calculator function which has 3 parameters - two numbers and a symbol for the math operation.
Example call to the function:
calculate(3, 5, '+')
which returns:
8

calculate(6, 2, '-')
which returns:
4

The supported operations are +, -, / and *
"""


def calculate(a,b,operation):
    if operation == '+':
        print(a + b)
    elif operation == '-':
        print(a - b)
    elif operation == '/':
        print(a / b)
    elif operation == '*':
        print(a * b)
a = float(input("enter first number: "))
operation = input("enter operation: ")
b = float(input("enter second number: "))
calc = calculate(a,b,operation)