print('''
        888                     888    
        888                     888    
        888                     888    
 .d8888b88888b.  .d88b. .d8888b 888888 
d88P"   888 "88bd8P  Y8b88K     888    
888     888  88888888888"Y8888b.888    
Y88b.   888  888Y8b.         X88Y88b.  
 "Y8888P888  888 "Y8888  88888P' "Y888 
''')
print("Welcome to Treasure Island."
"Your mission is to find the treasure.")
print("Where do you want to go?Left or Right.")
move = input()
if move == "Right":
    print("Fall into a hole.Game Over.")
elif move == "Left":
    print("swim or wait")
    move1 = input()
    if move1 == "swim":
        print("Attacked by trout.Game Over.")
    elif move1 == "wait":
        print("Which door?")
        move2 = input()
        if move2 == "Red":
            print("Burned by fire.Game Over.")
        elif move2 == "Yellow":
            print("You Win!")
        elif move2 == "Blue":
            print("Eaten by beasts.Game Over.")
        else:
            print("Game Over.")