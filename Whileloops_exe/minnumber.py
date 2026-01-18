import sys

minNumber = sys.maxsize
while True:
    number = input()
    if number == "Stop":
        break

    new_number = int(number)
    if new_number < minNumber:
        minNumber = new_number


print(minNumber)
