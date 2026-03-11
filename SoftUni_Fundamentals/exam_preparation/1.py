negative = []
positive = []
nums = list(map(int, input().split()))
for num in nums:
    if num < 0 :
        negative.append(num)
    else:
        positive.append(num)
print(negative)
print(positive)
print(f"Sum positive: {sum(positive)}")
print(f"Sum negative: {sum(negative)}")