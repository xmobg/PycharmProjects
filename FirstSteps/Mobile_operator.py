period_cont = input()
type_cont = input()
mobile_internet = input()
mounth_to_pay = int(input())
price = 0.0

if period_cont == 'one':
    if type_cont == 'Small':
        price += 9.98
    elif type_cont == 'Middle':
        price += 18.99
    elif type_cont == 'Large':
        price += 25.98
    elif type_cont == 'ExtraLarge':
        price += 35.99
elif period_cont == 'two':
    if type_cont == 'Small':
        price += 8.58
    elif type_cont == 'Middle':
        price += 17.09
    elif type_cont == 'Large':
        price += 23.59
    elif type_cont == 'ExtraLarge':
        price += 31.79

if mobile_internet == 'yes':
    if  price <= 10:
        price += 5.50
    elif price <= 30:
        price += 4.35
    elif price > 30:
        price += 3.85
if period_cont == 'two':
     price -= (price * 0.0375)

print(f"{price * mounth_to_pay:.2f} lv.")



