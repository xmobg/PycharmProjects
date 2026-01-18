number_of_masseges = int(input())
current_massage = ""
for massage in range(number_of_masseges):
    current_number = int(input())
    if current_number == 88:
        current_massage = "Hello"
    elif current_number == 86:
        current_massage = "How are you?"
    elif current_number < 88:
        current_massage = "GREAT!"
    else:
        current_massage= "Bye."
    print(current_massage)