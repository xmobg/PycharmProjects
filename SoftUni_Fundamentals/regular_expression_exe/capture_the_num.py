import re


pattern = r"\d+"

while True:
    try:
        text = input()
        ret = re.findall(pattern, text)
        for i in ret:
            print(i ,end=" ")
    except EOFError:
        break
