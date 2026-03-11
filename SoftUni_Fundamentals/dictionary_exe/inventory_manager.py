inventory_items = {}

while True:
    command = input()
    if command == "end":
        break

    item, quantity = command.split()
    quantity = int(quantity)

    if item not in inventory_items:
        inventory_items[item] = quantity
    else:
        inventory_items[item] += quantity

    if inventory_items[item] <= 0:
        del inventory_items[item]

for key, value in inventory_items.items():
    print(f"{key} -> {value}")
