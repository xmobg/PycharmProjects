import re

text = input()

pattern = r'\w+'

result = re.findall(pattern, text)
for word in result:
    print(word)

