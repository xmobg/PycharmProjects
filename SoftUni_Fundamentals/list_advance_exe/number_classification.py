numbers = input().split(", ")
positive_numbers = [number for number in numbers if int(number) >= 0]
print(f"Positive: {', '.join(positive_numbers)}")
negative_numbers = [number for number in numbers if int(number) < 0]
print(f"Negative: {', '.join(negative_numbers)}")
even_numbers = [number for number in numbers if int(number) % 2 == 0]
print(f"Even: {', '.join(even_numbers)}")
odd_number = [number for number in numbers if int(number) % 2 != 0]
print(f"Odd: {', '.join(odd_number)}")