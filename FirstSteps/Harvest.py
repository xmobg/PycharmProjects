import math
sqmeters_loze = int(input())
grape_sqmeter = float(input())
liters_need = int(input())
workers = int(input())

total_grape = sqmeters_loze * grape_sqmeter
wine = 0.40 * total_grape / 2.5

if wine > liters_need:
    print(f"Good harvest this year! Total wine: {math.ceil(wine)} liters.")
    print(f"{math.ceil(wine - liters_need)} liters left -> {math.ceil((wine - liters_need) / workers)} liters per person.")
else:
    print(f"It will be a tough winter! More {math.floor(liters_need - wine)} liters wine needed.")