needed_money = float(input())
balance = float(input())

number_days = 0
count_spanding_days = 0
is_enough_money = False


while count_spanding_days < 5:
    action = input()
    money = float(input())
    number_days += 1

    if action == "spend":
        count_spanding_days += 1
        balance = balance - money if balance > money else 0

    elif action == "save":
        count_spanding_days = 0
        balance += money

        if balance >= needed_money:
            is_enough_money = True
            break
if is_enough_money:
    print(f"You saved the money for {number_days} days.")
else:
    print("You can't save the money.")
    print(number_days)