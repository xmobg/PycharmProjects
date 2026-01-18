import math
from math import floor

days_off = int(input())
food_leavet = int(input())
food_for_dog = float(input())
food_for_cat = float(input())
food_for_turtle = float(input()) / 1000

total_food = (days_off * food_for_dog) + (days_off * food_for_cat) + (days_off * food_for_turtle)
if total_food < food_leavet:
    print(f"{floor(food_leavet - total_food)} kilos of food left.")
elif total_food > food_leavet:
    print(f"{math.ceil(total_food - food_leavet)} more kilos of food are needed.")