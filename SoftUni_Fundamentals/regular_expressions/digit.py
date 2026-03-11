import re

text = input()

pattern = r"(^|(?<=\s))-?(0|[1-9]\d*)(\.\d+)?($|(?=\s))"

matches = re.finditer(pattern, text)

result = []

for match in matches:
    result.append(match.group())

print(" ".join(result))