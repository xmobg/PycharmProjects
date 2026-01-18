# Task: Word Length Counter
# Write a function word_length_counter that takes a list of words as input and returns a dictionary
# where the keys are the lengths of the words and the values are lists of words of that length.


def word_length_counter(words):
    result = {}

    for word in words:
        length = len(word)
        if length not in result:
            result[length] = []
        result[length].append(word)

    return result

words = ["apple", "car", "python", "sun", "hello", "go"]
print(word_length_counter(words))
