"""Create a list with shopping items. Ask the user for a shopping item.
If the item is already on the list print it, and
if not - add it to the list and then print "{item} added to the list!"."""
adding_to_list = True
ask_user_for_shopping_list = " "
shopping_list = []
while adding_to_list == True :
    item_for_shopping_list = input("Enter a shopping item: ")
    if  item_for_shopping_list not in shopping_list:
        shopping_list.append(item_for_shopping_list)
        print(f"{item_for_shopping_list} added to the shopping list!")
    elif item_for_shopping_list in shopping_list:
        print(f"{item_for_shopping_list} already on the shopping list!")
    print("Do you still want to add items to shopping list?")
    ask_user_for_shopping_list = input("Y or N: ").upper()
    if ask_user_for_shopping_list == "N":
        break





