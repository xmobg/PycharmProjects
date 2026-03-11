total_price = 0.0
tax = 0.0
discount = 0.10
customer_type = ""

while True:
    price = input()

    if price == "special" or price == "regular":
        customer_type = price
        break

    if float(price) < 0:
        print("Invalid price!")
        continue

    total_price += float(price)


if total_price == 0:
    print("Invalid order!")
    exit()

tax = total_price * 0.20
final_price = total_price + tax

if customer_type == "special":
    final_price -= final_price * discount

print("Congratulations you've just bought a new computer!")
print(f"Price without taxes: {total_price:.2f}$")
print(f"Taxes: {tax:.2f}$")
print("-----------")
print(f"Total price: {final_price:.2f}$")
