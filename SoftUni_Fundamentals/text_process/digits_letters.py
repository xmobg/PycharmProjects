text = input()

letters = ""
digits = ""
charts = ""

for char in text:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
    else:
        charts += char


print(digits)
print(letters)
print(charts)
