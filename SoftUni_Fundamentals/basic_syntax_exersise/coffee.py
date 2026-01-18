coffes = 0
while  True:
    events = input()
    if events == "END":
        break
    elif events == "coding":
        coffes += 1
    elif events == "CODING":
        coffes += 2
    elif events == "dog":
        coffes += 1
    elif events == "DOG":
        coffes += 2
    elif events == "cat":
        coffes += 1
    elif events == "CAT":
        coffes += 2
    elif events == "movie":
        coffes += 1
    elif  events == "MOVIE":
        coffes += 2
if coffes > 5 :
    print(f"You need extra sleep")
else:
    print(coffes)