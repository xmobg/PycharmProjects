text = input()
lower_text = text.lower()
words = ["sand", "water", "fish", "sun"]
count = 0
for word in words:
    count += lower_text.count(word)
print(count)