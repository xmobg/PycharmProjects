some_text = input()

sorted_text = [ch for ch in some_text if ch.lower() not in ["a","e","i","o","u"]]
print("".join(sorted_text))
