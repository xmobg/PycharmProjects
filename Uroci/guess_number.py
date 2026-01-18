"""
Write a program that sets a secret number e.g. 37
Ask the user to guess the number and provide feedback on whether their guess is too high, too low, or correct.
Repeat until the user guesses correctly or gives up.
"""
secret_number = 37
number_guesses = int(input("Enter the number of guesses: "))
if secret_number == number_guesses:
    print("Correct!")
while secret_number != number_guesses:
    if secret_number < number_guesses:
        print("Too high!")
        number_guesses = int(input("Enter the number of guesses: "))

    elif secret_number > number_guesses:
        print("Too low!")
        number_guesses = int(input("Enter the number of guesses: "))
    if secret_number == number_guesses:
        print("Correct!")
