fruits = ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"]
vegi = ["tomato", "cucumber", "pepper", "carrot"]
what_it_is = input()

if what_it_is in fruits:
    print("fruit")
elif what_it_is in vegi:
    print("vegetable")
else:
    print("unknown")