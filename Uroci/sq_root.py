import math
try:
    number_root = int(input("Enter a number: "))
    print(math.sqrt(number_root))
except ValueError:
    print("Please enter a number!")

