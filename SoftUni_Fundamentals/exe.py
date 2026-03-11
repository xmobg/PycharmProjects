
my_list = [9, 12, 3, 5, 14, 10, 10]
less_than_10 = []
equal_10 = []
greater_than_10 = []

for element in my_list:
    if element < 10:
        less_than_10.append(element)
    elif element == 10:
        equal_10.append(element)
    else:
        greater_than_10.append(element)
new_list = less_than_10 + equal_10 + greater_than_10
print(new_list)




