words = ["apple", "banana", "apple", "orange", "banana", "apple"]

words_count = {}

for word in words:
   words_count[word] = words_count.get(word, 0) + 1

for key,value in words_count.items():
    print(f"{key} - {value}")
