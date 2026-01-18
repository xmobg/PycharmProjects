"""
Create a program that asks the user to enter game scores for three players.
Print the highest score and the player who achieved it.
"""

player_one = int(input("Enter the first player's score: "))
player_two = int(input("Enter the second player's score: "))
player_three = int(input("Enter the third player's score: "))

while player_one != player_two and player_one != player_three:

    if player_one > player_two and player_one > player_three:
        print(f"player one have biggest score: {player_one}")
        break
    elif player_two > player_one and player_two > player_three:
        print(f"player two have biggest score: {player_two}")
        break
    else:
        print(f"player three have biggest score: {player_three}")
        break



