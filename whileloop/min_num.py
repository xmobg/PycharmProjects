import sys

min_num = sys.maxsize

while True:
    new_imput = input()
    if new_imput == "Stop":
        break

    number = int(new_imput)
    if number < min_num:
        min_num = number

print(min_num)