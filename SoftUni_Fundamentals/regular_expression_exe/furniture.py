import re

total_cost = 0
brought_furniture  = []

pattern = r">>([a-z]+)<<(\d+\.?\d*)!(\d+)"
command = input()
while command != "Purchase":
    match = re.search(pattern, command, re.IGNORECASE)
    if match:
        furniture_name,price,quantity = match.groups()
        brought_furniture.append(furniture_name)
        total_cost += float(price) * int(quantity)
    command = input()
print("Bought furniture:")
for furniture in brought_furniture:
    print(furniture)
print(f"Total money spend: {total_cost:.2f}")
