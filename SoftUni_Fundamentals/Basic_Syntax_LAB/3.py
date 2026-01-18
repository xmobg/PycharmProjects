animals = input().split(", ")

wolf_index = animals.index("wolf")
sheep_after_wolf = len(animals) - wolf_index - 1

if sheep_after_wolf == 0:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {sheep_after_wolf}! You are about to be eaten by a wolf!")
