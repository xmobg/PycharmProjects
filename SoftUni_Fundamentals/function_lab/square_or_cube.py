def square_or_cube(number , text):
    if text == "cube":
        return number ** 3
    elif text == "square":
        return number ** 2
    else:
        return ("Invalid input")
number = int(input())
power_text = input()
result = square_or_cube(number , power_text)
print(result)
