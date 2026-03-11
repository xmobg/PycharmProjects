def all_char(first_character = str, second_character = str):
    char = []
    for characters in range(ord(first_character)+1, ord(second_character)):
        char.append(chr(characters))
    return char
first_char = input()
second_char = input()
result = all_char(first_char, second_char)
print(" ".join(result))