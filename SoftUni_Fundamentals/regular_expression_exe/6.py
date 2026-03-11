import re

text = input()

pattern = r'[A-Z][a-z]+'

result = re.findall(pattern, text)
for i in result:
    print(i)
