grades = [55, 23, 87, 39, 100, 72, 18, 44, 67, 32, 90, 25, 61]
failing_count = 0

for grade in grades:
    if grade < 40:
        failing_count += 1


print("Number of failing grades:", failing_count)
