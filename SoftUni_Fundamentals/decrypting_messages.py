key = int(input())
lines = int(input())
massage = ""
for i in range(lines):
    char = input()
    new_char = chr(ord(char) + key)
    massage += new_char
print(massage)