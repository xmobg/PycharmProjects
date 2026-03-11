words = {}
word = input()

for char in word:
    if char == " ":
        continue
    words[char] = words.get(char, 0) + 1
for key,value in words.items():
    print(f"{key} -> {value}")