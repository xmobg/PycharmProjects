number = list(map(int, input().split()))
average_number = sum(number) / len(number)
greater_than_average = [x for x in number if average_number < x]
if greater_than_average:
    print("No")
else:
    top_five = sorted(greater_than_average, reverse=True)[:5]
    print(" ".join(map(str, top_five)))