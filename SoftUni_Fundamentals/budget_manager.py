expenses = list(map(int, input().split()))
over_fifty_total = []
over_fifty = 0
for expense in expenses:
    if expense > 50:
        over_fifty += 1
        over_fifty_total.append(expense)
print(f"Брой разходи над 50: {over_fifty}")
print(f"Обща сума на разходите над 50: {sum(over_fifty_total)}")