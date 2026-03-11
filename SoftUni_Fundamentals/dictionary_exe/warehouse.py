warehouse = {}

while True:
    command = input()
    if command == "end":
        break

    product,quantity = command.split()
    quantity = int(quantity)
    if product not in warehouse:
        warehouse[product] = quantity
    else:
        warehouse[product] += quantity
    if warehouse[product] <= 0:
        del warehouse[product]
for key,value in warehouse.items():
    print(f"{key} -> {value}")