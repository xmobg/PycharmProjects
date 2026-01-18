def char_frequency(text):
    freq = {}

    for char in text:
        if char == " ":
            continue

        if char not in freq:
            freq[char] = 0
        freq[char] += 1

    return freq

print(char_frequency("hello world"))