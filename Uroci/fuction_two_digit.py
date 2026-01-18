"""
Write a function which accepts 1 parameter and checks if the number is two-digit number. The function must return True or False (boolean type)

Let the user enter a number and then print "Valid" if the number is two-digit one (use the function to check) or "Invalid" accordingly.
"""

def number_digits():
    n = int(input("Enter a number: "))
    if  n < 10:
        print("Valid")
        return True
    else:
        print("Invalid")
        return False


number_digits()