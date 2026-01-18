budget = float(input())
petrolium_need = float(input()) * 2.10 + 100
day_of_week = input(" ")

if day_of_week == "Sunday":
    petrolium_need = petrolium_need - (petrolium_need * 0.20)
    if budget >= petrolium_need:
        print(f"Safari time! Money left: {abs(budget - petrolium_need):.2f} lv.")
    else:
        print(f"Not enough money! Money needed: {abs(budget - petrolium_need):.2f} lv.")

elif day_of_week == "Saturday":
    petrolium_need = petrolium_need - (petrolium_need * 0.10)
    if budget >= petrolium_need:
        print(f"Safari time! Money left: {abs(budget - petrolium_need):.2f} lv.")
    else:
        print(f"Not enough money! Money needed: {abs(budget - petrolium_need):.2f} lv.")
