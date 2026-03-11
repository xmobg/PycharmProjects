products = {}

while True:
    command = input()

    if command == "buy":
        break

    name, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if name not in products:
        products[name] = [price, quantity]
    else:
        products[name][1] += quantity
        products[name][0] = price

for product, data in products.items():
    total_price = data[0] * data[1]
    print(f"{product} -> {total_price:.2f}")