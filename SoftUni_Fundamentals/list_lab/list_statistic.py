positive_number = []
negative_number = []
number = int(input())
for i in range(number):
    number = int(input())
    if number >= 0 :
        positive_number.append(number)
    else:
        negative_number.append(number)

print(positive_number)
print(negative_number)
print(f"Count of positives: {len(positive_number)}")
print(f"Sum of negatives: {sum(negative_number)}")