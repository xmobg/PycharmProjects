try:
    colors = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta']
    user_choice = int(input("Enter your choice: "))
    print(colors[user_choice])
except IndexError:
    print("Please enter other number!")