money = float(input())
target_year = int(input())
age = 17
start_year = 1800
for year in range(start_year , target_year + 1):
    age += 1
    if year % 2 == 0:
        money -=12000
    else:
        money -= (12000 + (50 * age))



if money >= 0 :
    print(f"Yes! He will live a carefree life and will have {money:.2f} dollars left.")
else:
    print(f"He will need {abs(money):.2f} dollars to survive.")