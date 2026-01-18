import random
options = ["rock", "paper", "scissors"]
computer_score = 0
user_score = 0
print("Welcome to the Rock Paper Scissors game!")
print("Type 'quit' to exit")

while True:

    user_choice = input("Enter your choice: rock, paper, or scissors: ").lower()
    if user_choice == "quit":
        print("Thanks for playing! Goodbye!")
        print(f"Final score is user:{user_score}/computer:{computer_score}")
        break

    if user_choice not in options:
        print("Invalid choice! Try again!")
        continue

    computer_choice = random.choice(options)
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("Its a tie!")

    elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1