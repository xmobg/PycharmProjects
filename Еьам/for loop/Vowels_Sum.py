points =0
sequence = input()
for char in sequence:
    if char == 'a':
        points += 1
    elif char == 'e':
        points += 2
    elif char == 'i':
        points += 3
    elif char == 'o':
        points += 4
    elif char == 'u':
        points += 5
print(points)