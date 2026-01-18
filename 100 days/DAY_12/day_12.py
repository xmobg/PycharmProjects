import random
def easy_game():
    counter = 10
    number_to_guess = random.randint(1, 100)
    while counter >= 0:
        guessed_number = int(input("Guess a number between 1 and 100: "))
        print(number_to_guess)
        if guessed_number == number_to_guess:
            print("You win!")
            break
        elif guessed_number > number_to_guess:
            print("Too high!")
            counter = counter - 1
            print(f"You have {counter} guesses left.")
        elif guessed_number < number_to_guess:
            print("Too low!")
            counter = counter - 1
            print(f"You have {counter} guesses left.")
        elif counter == 0:
            print("You lose!")
def hard_game():
    counter = 5
    number_to_guess = random.randint(1, 100)
    while counter >= 0:
        guessed_number = int(input("Guess a number between 1 and 100: "))
        print(number_to_guess)
        if guessed_number == number_to_guess:
            print("You win!")
            break
        elif guessed_number > number_to_guess:
            print("Too high!")
            counter = counter - 1
            print(f"You have {counter} guesses left.")
        elif guessed_number < number_to_guess:
            print("Too low!")
            counter = counter - 1
            print(f"You have {counter} guesses left.")
        elif counter == 0:
            print("You lose!")
game_mode = input("Chose a mode: ")
while game_mode == "easy" or game_mode == "hard":
    if game_mode == "easy":
        easy_game()
    elif game_mode == "hard":
        hard_game()
    else:
        print("Please choose a mode.")