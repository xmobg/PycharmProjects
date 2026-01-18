import random
computer_wins = 0
user_wins = 0
print("Welcome to the Dice Game!")
continue_play = " "
while continue_play != "N":
    computer_dice_one = random.randint(1, 6)
    computer_dice_two = random.randint(1, 6)
    user_dice_one = random.randint(1, 6)
    user_dice_two = random.randint(1, 6)
    print(f"Computer rolls: {computer_dice_one}  {computer_dice_two}  = {computer_dice_one+computer_dice_two}" )
    print(f"User rolls: {user_dice_one}  {user_dice_two}  = {user_dice_one+user_dice_two} " )
    if (computer_dice_one + computer_dice_two) > (user_dice_one + user_dice_two):
        print("Computer wins!")
        computer_wins += 1
    else:
        print("You win!")
        user_wins += 1
    continue_play = input("Do you want to play again? (Y/N): ")
    continue_play = continue_play.upper()
    if continue_play.lower() == "n":
        print("Thank you for playing!")
        print(f"Computer wins {computer_wins} , your wins {user_wins}")