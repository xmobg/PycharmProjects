phone_book = {}
while True:
    entry = input()
    if "-" not in entry:
        break
    name,number = entry.split("-")
    phone_book[name] = number
search_number = int(entry)
for search in range(search_number):
    seached_name = input()
    if seached_name in phone_book.keys():
        print(f"{seached_name} -> {phone_book[seached_name]}")
    else:
        print(f"Contact {seached_name} does not exist.")