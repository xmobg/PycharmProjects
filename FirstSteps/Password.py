user_name = input()
passwort = input()

while True:
    passwort_try = input()
    if passwort == passwort_try:
        print("Welcome " + user_name +"!")
        break
