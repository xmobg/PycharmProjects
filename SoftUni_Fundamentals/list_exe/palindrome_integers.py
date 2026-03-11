my_list = list(map(int,input().split(", ")))


for num in my_list:
    res = str(num) == str(num)[::-1]
    print(res)