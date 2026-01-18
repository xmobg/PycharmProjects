kilometers_to_travel = int(input())
day_or_night = input()
price_to_pay = 0.0
if kilometers_to_travel <= 19 and day_or_night == "day":
    price_to_pay = 0.70 + kilometers_to_travel * 0.79
    print(f"{price_to_pay:.2f}")
elif kilometers_to_travel <= 19 and day_or_night == "night":
    price_to_pay = 0.70 + kilometers_to_travel * 0.90
    print(f"{price_to_pay:.2f}")
elif 100 > kilometers_to_travel >= 20:
    price_to_pay = kilometers_to_travel * 0.09
    print(f"{price_to_pay:.2f}")
elif kilometers_to_travel >= 100:
    price_to_pay = kilometers_to_travel * 0.06
    print(f"{price_to_pay:.2f}")