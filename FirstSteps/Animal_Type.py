animal = input()
animal_type = ""
reptile = ["crocodile" , "tortoise" , "snake"]
if animal == "dog":
    animal_type = "mammal"
    print(animal_type)
elif animal in reptile:
    animal_type = "reptile"
    print(animal_type)
else:
    animal_type = "unknown"
    print(animal_type)


