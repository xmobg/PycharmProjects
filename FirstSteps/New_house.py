type_flower = input()
number_of_flower = int(input())
budget = int(input())
sum_flowers = 0.0
ROSE = 5
DALIA = 3.80
TULIPA = 2.80
NARCIS = 3
GLADIOLA = 2.50
DISCOUNT_ROSE = 0.10
DISCOUNT_DALII= 0.15
DISCOUNT_TULIPA = 0.15
DISCOUNT_NARCIS = 0.15
DISCOUNT_GLADIOLA = 0.20
if type_flower == "Roses":
    sum_flowers = number_of_flower * ROSE


    if number_of_flower > 80:
        sum_flowers -=(sum_flowers * DISCOUNT_ROSE)

elif type_flower == "Dahlias":
    sum_flowers = number_of_flower * DALIA

    if number_of_flower > 90:
        sum_flowers -=(sum_flowers * DISCOUNT_DALII)

elif type_flower == "Tulips":
    sum_flowers = number_of_flower * TULIPA

    if number_of_flower > 80:
        sum_flowers -=(sum_flowers * DISCOUNT_TULIPA)

elif type_flower == "Narcissus":
    sum_flowers = number_of_flower * NARCIS

    if number_of_flower < 120:
        sum_flowers += (sum_flowers * DISCOUNT_NARCIS)

elif type_flower == "Gladiolus":
    sum_flowers = number_of_flower * GLADIOLA
    if number_of_flower < 80:
        sum_flowers += (sum_flowers * DISCOUNT_GLADIOLA)

if budget >= sum_flowers:
        print(f"Hey, you have a great garden with {number_of_flower} {type_flower} and {budget - sum_flowers:.2f} leva left.")
else:
        print(f"Not enough money, you need {sum_flowers - budget:.2f} leva more.")


