import re

date = input()

pattern = r'\d{2}/\d{2}/\d{4}'

result = re.findall(pattern, date)
for item in result:
    print(item)

