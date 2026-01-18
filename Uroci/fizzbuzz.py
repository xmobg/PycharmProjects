"""
Write a program that prints the number that the user entered.
But for multiples of three, print "Fizz" instead of the number,
and for the multiples of five, print "Buzz."
For numbers that are multiples of both three and five, print "FizzBuzz."
"""


def fizzbuzz(n):
    result = []
    for x in range(1, n+1):
        if x % 3 == 0 and x % 5 == 0:
            result.append("fizz buzz")
        elif x % 3 == 0:
            result.append('fizz')
        elif x % 5 == 0:
            result.append('buzz')
        else:
            result.append(str(x))
    return result
user_number = int(input("Enter a number: "))
def main():
    print(', '.join(fizzbuzz(user_number)))

main()