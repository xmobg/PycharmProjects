unit = input("Please enter your unit: C/F ")
temp = float(input("Please enter your temperature: "))
if unit == "F":
    temp = (temp * 9) / 5 + 32
    print(f"The temperature in F is: {temp:.2f}°F ")
elif unit == "C":
    temp = (temp - 32) * 5 /9
    print(f"The temperature in C is: {temp:.2f}°C")
else:
    print("Please enter a unit")
