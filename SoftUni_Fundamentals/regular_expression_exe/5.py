import re
phone_num = input()

pattern = r"\+359([ -])2\1\d{3}\1\d{4}\b"

result = re.findall(pattern, phone_num)
print(result)


