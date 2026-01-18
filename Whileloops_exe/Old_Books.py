searched_books = input()

checked_books = 0
book_name = input()

while book_name != searched_books and book_name != "No More Books":
    checked_books += 1
    book_name = input()
if book_name == searched_books:
    print(f"You checked {checked_books} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {checked_books} books.")