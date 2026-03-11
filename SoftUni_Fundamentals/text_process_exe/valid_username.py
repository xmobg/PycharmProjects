def lenght_valid(name):
    if 3 <= len(name) <= 16:
        return True
    return False
def symbol_valid(name):
    for char in name:
        if not (char.isalnum() or char == '-' or char == '_'):
            return False
    return True
def synbols(name):
    if " " in name:
        return False
    return True
def username_valid(name):
    if lenght_valid(name) and symbol_valid(name) and synbols(name):
        return True
    return False

user_names = input().split(", ")
for username in user_names:
    if username_valid(username):
        print(username)