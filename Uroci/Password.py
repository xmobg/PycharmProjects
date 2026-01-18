"""
Implement a simple password checker using a while loop.
Keep prompting the user for a password until they enter the correct one.
The correct password is '12345'
"""
password = "12345"
password_check = input("Enter the password: ")
while password_check != password:
    print("Incorrect password")
    password_check = input("Enter the password: ")
    if password_check == password:
        print("Correct")
