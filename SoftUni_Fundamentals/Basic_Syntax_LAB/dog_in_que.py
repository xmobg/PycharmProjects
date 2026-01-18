animals = input().split(",")
dog_index = animals.index("dog")
if dog_index == 0:
    print("Dog is already at the front!")
else:
    print(f"Dog is number {dog_index} in the queue")