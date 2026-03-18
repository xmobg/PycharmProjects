import re
pattern = r"(w{3}\.[a-z0-9\-]+(\.[a-z]+)+)"
line = input()
while line:
    match = re.search(pattern, line, re.IGNORECASE)
    if match:
        link = match.group(1)
        print(link)
    line = input()
