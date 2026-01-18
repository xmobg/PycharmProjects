"""
Create a Shopping List Application

Define an empty list to store shopping items.

Write a function to add items to the shopping list.
Prompt/Ask the user for items and append them to the list.

Write a function to display the current shopping list sorted ascending.

Write a function to remove items from the shopping list.
Prompt the user for items to remove and remove them from the list.

Write a function to calculate the total cost of items in the shopping list.
Assume each item has the same price - $5

Write a function to mark items as purchased.
Prompt the user for items to check off and remove them from the list.

Sample Program Output:

1. Add Items
2. View List
3. Remove Items
4. Calculate Total Cost
5. Check Off Items
6. Exit
Enter your choice (1-6):
"""

shopping_list = []
price_per_item = 5
def adding_items_to_shopping_list():
    print("Adding Items to Shopping List")
    while True:
        item = input("Enter Item to add: ")
        print(f"{item} added to Shopping List.If you finish please write No")
        if item == "No":
            break
        shopping_list.append(item)

def viewing_list_from_shopping_list():
    if not shopping_list:
        print("No items added to Shopping List")
    else:
        for item in shopping_list:
            print("*",item)

def remove_items_from_shopping_list():
    for items in shopping_list:
        print("*",items)
    item = input("Enter Item to remove or write No to go back to menu ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from Shopping List")
    elif item == "No":
        return
    else:
        print("Item not in Shopping List")
def calculating_total_cost():
    total_items = len(shopping_list)
    total_cost = total_items * price_per_item
    print(f"Total cost: {total_cost}")
def check_off_items():
    for items in shopping_list:
        print("*",items)
    item = input("Enter Item to check: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from Shopping List")
    else:
        print("Item not in Shopping List")

while True:
    print("\n1. Add Items")
    print("2. View List")
    print("3. Remove Items")
    print("4. Calculate Total Cost")
    print("5. Check Off Items")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        adding_items_to_shopping_list()
    elif choice == "2":
        viewing_list_from_shopping_list()
    elif choice == "3":
        remove_items_from_shopping_list()
    elif choice == "4":
        calculating_total_cost()
    elif choice == "5":
        check_off_items()
    elif choice == "6":
        print("End of program")
        break
    else:
        print("Wrong Choice")