def filter_string(words,n):
    result = [word for word in words if len(word) > n]
    return result
words = ["cat", "elephant", "sun", "dictionary"]

print(filter_string(words,3))