weight = float(input("Please enter a weight: "))
unit = input("Kilograms or Pounds? (Kg, Lbs): " )
if unit == "Lbs":
    weight = weight * 2.205
    print(f"The weight is: {weight:.2f}  {unit}.")
elif unit == "Kg":
    weight = weight  / 2.205
    print(f"The weight is: {weight:.2f}  {unit}.")
else:
    print("Please enter a valid unit")



