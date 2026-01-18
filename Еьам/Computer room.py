
month = input().lower()
hours = int(input())
people = int(input())
time_of_day = input().lower()


price_per_hour = 0

if month in ["march", "april", "may"]:
    if time_of_day == "day":
        price_per_hour = 10.50
    elif time_of_day == "night":
        price_per_hour = 8.40
elif month in ["june", "july", "august"]:
    if time_of_day == "day":
        price_per_hour = 12.60
    elif time_of_day == "night":
        price_per_hour = 10.20


if people >= 4:
    price_per_hour *= 0.90
if hours >= 5:
    price_per_hour *= 0.50


price_per_person_per_hour = price_per_hour
total_price = price_per_person_per_hour * hours * people
print(f"Price per person for one hour: {price_per_person_per_hour:.2f}")
print(f"Total cost of the visit: {total_price:.2f}")