price_vegi_for_kg = float(input())
price_fruit_for_kg = float(input())
total_vegi = float(input())
total_fruit = float(input())
total_kg = ((price_vegi_for_kg * total_vegi) + (price_fruit_for_kg * total_fruit)) / 1.94
print(f"{total_kg:.2f}")