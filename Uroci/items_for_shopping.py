"""Create a list with shopping items. Ask the user for a shopping item and
if they want to add or remove it from the list.
 If the item is already on the list and they want to add it, print "{item} already on the list. Nothing to add.".
 If they want to remove an item which is not on the list, print "{item} not on the list. Nothing to remove."."""
adding_to_list = True
ask_user_for_shopping_list = " "
shopping_list = []
adding_or_removbing = " "
while adding_to_list == True :
    adding_to_list = input("Are you adding or removing an item? A is for Adding and R is for Removing.").upper()
    if adding_to_list == "A":
        item_for_shopping_list = input("Enter a shopping item: ")
        if  item_for_shopping_list not in shopping_list:
            shopping_list.append(item_for_shopping_list)
            print(f"{item_for_shopping_list} added to the shopping list!")
        elif item_for_shopping_list in shopping_list:
            print(f"{item_for_shopping_list} already on the list. Nothing to add.")
    elif adding_to_list == "R":
        item_for_shopping_list = input("Enter the removing item: ")
        shopping_list.remove(item_for_shopping_list)
        print(f"{item_for_shopping_list} removed from the shopping list!")
    if item_for_shopping_list not in shopping_list:
        print(f"{item_for_shopping_list} not on the list. Nothing to remove.")
    print("Do you still want to add items to shopping list?")
    ask_user_for_shopping_list = input("Y or N: ").upper()
    if ask_user_for_shopping_list == "N":
        adding_to_list = False
    elif ask_user_for_shopping_list == "Y":
        adding_to_list = True
        continue