import random

def guess_the_number():
  random_number = random.randint(1,100)
  max_attempts = 5
  while max_attempts != 0:
    user_guess = int(input("Guess the number: "))
    if random_number == user_guess:
     print("You guess the number,nice job!")
     break
    elif user_guess > random_number:
      print(f"Your number is higher \n You have {max_attempts - 1} attempts left!")
    else:
      print(f"Your number is lower  \n You have {max_attempts - 1} attempts left!")
    max_attempts -= 1
  if max_attempts == 0:
    print(f"Game Over, the number was {random_number}")
guess_the_number()