price_toy = 5
price_sweater = 15

count_kids = 0
count_adults = 0

while True:
    line = input()
    if line == "Christmas":
        break
    age = int(line)
    if age <= 16:
        count_kids += 1
    else:
        count_adults += 1

money_for_toys = count_kids * price_toy
money_for_sweaters = count_adults * price_sweater


print(f"Number of adults: {count_adults}")
print(f"Number of kids: {count_kids}")
print(f"Money for toys: {money_for_toys}")
print(f"Money for sweaters: {money_for_sweaters}")