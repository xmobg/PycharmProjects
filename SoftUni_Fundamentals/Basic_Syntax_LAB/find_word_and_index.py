text = input()
lower_text = text.lower()
words = ["rose","tulip","daisy","sunflower"]
total_count = 0
for word in words:
    position = []
    start = 0
    while True:
        index = lower_text.find(word, start)
        if index == -1:
            break
        position.append(index)
        start = index + 1
        total_count += 1
    if position:
        print(f"'{word}' found at positions: {position}")
print(f"Total count: {total_count}")