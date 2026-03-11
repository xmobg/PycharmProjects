text = input()
encrypted_text = ""

for char in text:
    encrypt_char =chr(ord(char) + 3)
    encrypted_text += encrypt_char
print(encrypted_text)
