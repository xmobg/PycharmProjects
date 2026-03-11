def positive_or_negative(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"
a = int(input())
result = positive_or_negative(a)
print(result)