char = input()
occurrences = {}
for char in char:
    if char == " ":
        continue
    occurrences[char] = occurrences.get(char, 0) + 1
for char , repetitions in occurrences.items():
    print(f"{char} -> {repetitions}")
