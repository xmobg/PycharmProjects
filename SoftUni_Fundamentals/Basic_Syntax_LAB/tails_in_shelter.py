animals = input().split(", ")

if animals[0] == "dog":
    print("Dog is already at the front!")
elif animals[0] == "rabbit":
    print("Rabbit is first in line, watch out!")
elif animals[0] == "cat":
    if "dog" in animals:
        dog_index = animals.index("dog")
        print(f"Dog is number {dog_index} in the queue")
    else:
        print("No dogs in the queue")