numbers = input()
if numbers[0]== "-":
    digits = list(numbers[1:])
    digits.sort()
    sorted_number = "-" + "".join(digits)
else:
    digits = list(numbers)
    digits.sort(reverse=True)
    sorted_number = "".join(digits).lstrip("0")
print(sorted_number)