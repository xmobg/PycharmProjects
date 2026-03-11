data = input().split()

coocking_list = {}

for i in range(0,len(data), 2):
    food = data[i]
    quantity = int(data[i+1])
    coocking_list[food] = quantity

print(coocking_list)
