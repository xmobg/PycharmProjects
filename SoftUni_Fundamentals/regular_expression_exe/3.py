import re

text = input()

pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}'
result = re.findall(pattern, text)
print(' '.join(result))
