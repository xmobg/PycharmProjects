import random


scissors = '''
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''

rock = '''

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
random_number = random.randint(0, 2)

choice = int(input())

game_img = [rock, paper, scissors]
if choice >= 0 and choice <= 2:
    print(game_img[choice])

print(game_img[random_number])
if choice >= 3 or choice < 0 :
    print("You chose an invalid number.")

elif choice == 0 and random_number == 2:
    print("You win!")
elif random_number == 0 and choice == 2:
    print("You lose!")
elif random_number > choice:
    print("You lose!")
elif choice > random_number:
    print("You win!")

