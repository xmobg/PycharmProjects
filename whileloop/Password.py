username =input()
password = input()

while True:
    new_password = input()
    if new_password != password:
        pass
    else:
        print(f"Welcome {username}!")
        break