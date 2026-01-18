text = input()
upper_case_char = []

for i in range(len(text)):
    if text[i].isupper():
        upper_case_char.append(i)

print(upper_case_char)