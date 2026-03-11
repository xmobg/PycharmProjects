money_as_string = input().split(", ")
number_of_beggers = int(input())
money_as_integer = []
for money in money_as_string:
    money_as_integer.append(int(money))
beggers_sum = []
start_index = 0
for current_begger in range(number_of_beggers):
    current_begger_sum = 0
    for index in range(start_index, len(money_as_integer),number_of_beggers):
        current_begger_sum += money_as_integer[index]
    beggers_sum.append(current_begger_sum)
    start_index += 1
print(beggers_sum)