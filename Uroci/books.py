"""
Ask the user to enter the number of books they want to purchase and the total cost.
If they are buying
at least 5 books or spending over $50, offer a 10% discount. Print the final cost.
"""
books_to_purchase = int(input("How many books would you like to buy? "))
total_cost = int(input("What will be the total cost? "))
discount = total_cost * 0.10
if books_to_purchase >= 5 or total_cost >= 50:
    total_cost -= discount
    print(total_cost)
else:
    print(total_cost)