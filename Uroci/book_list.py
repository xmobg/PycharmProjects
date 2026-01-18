"""
Create an empty list named books.
Ask the user to input the titles of their favorite books one by one and add them to the list.
Print the final list of books sorted in ascending and then in descending order.
"""

books = []
continue_program = " "
while True:
    favorite_book = input("Enter a favorite book: ")
    if favorite_book not in books:
        books.append(favorite_book)
    continue_program = input("Do you want to add another book? (y/n)")
    if continue_program == "n":
        break
sorted_books = sorted(books)
reversed_books = sorted(books,reverse=True)
print(f"There are {sorted_books} favorite books.")
print(f"There are reversed {reversed_books} favorite books.")