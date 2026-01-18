import sys
maxNumber = -sys.maxsize
while True:
    news_input = input()
    if news_input == "Stop":
        break

    number = int(news_input)
    if number > maxNumber:
        maxNumber = number

print(maxNumber)