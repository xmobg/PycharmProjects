prize_for_pizza = 0
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want?S,M or L:")
pepperoni = input("Do you want pepperoni on your pizza?Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
if size == "S":
    prize_for_pizza = 15


elif size == "M":
    prize_for_pizza = 20

elif size == "L":
    prize_for_pizza = 25

else:
    print("Wrong Input")

if pepperoni == "Y":
    if size == "S":
        prize_for_pizza += 2
    else:
        prize_for_pizza += 3

if extra_cheese == "Y":
    prize_for_pizza += 1

print(prize_for_pizza)