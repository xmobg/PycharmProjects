budget = float(input())
flour_price = float(input())
egg_pack = 0.75 * flour_price
milk_price_for_liter = flour_price * 1.25
milk_price_per_bread = milk_price_for_liter * 0.25
bread_price = milk_price_per_bread + egg_pack + flour_price
loaves = 0
colored_eggs = 0
while budget >= bread_price:
    budget -= bread_price
    loaves += 1
    colored_eggs += 3
    if loaves % 3 == 0:
        colored_eggs -=(loaves - 2)

print(
    f"You made {loaves} loaves of Easter bread! "
    f"Now you have {colored_eggs} eggs and {budget:.2f}BGN left."
)

