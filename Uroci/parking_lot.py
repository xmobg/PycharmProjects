"""
Create a basic parking lot with a limited number of spaces e.g. 10 spaces.
Ask the user if they want to enter or exit the parking lot, or quit the program.
Users can enter the parking lot until it is full; and also exit the parking lot.
The program will inform users about the current status of the parking lot e.g.

Current Parking Lot Status: 8 free spaces.
"""
free_space = 8
user_choice = " "
while True:
    user_choice = input("Please enter your choice,do you want to enter,exit or quit: ")

    if user_choice.lower() == "enter":
        if free_space == 0:
            print("Theres no space left\n come back later")
        else:
            print(f"Come in, there is {free_space} parking spot left")
            free_space -= 1
    elif user_choice.lower() == "exit":
        free_space += 1
        print("Thank you,come again")
    elif user_choice.lower() == "quit":
        print("bye bye")
        break
    else:
      print("Incorect input")
