import math
processors_to_do = int(input())
employess = int(input())
hours_to_work = int(input())

working_to_work = employess * hours_to_work * 8
cpu_to_build = math.floor(working_to_work / 3)

if cpu_to_build < processors_to_do:
    procesors_needed = processors_to_do - cpu_to_build
    loses = procesors_needed * 110.10
    print(f"Losses: -> {loses:.2f} BGN")
elif cpu_to_build > processors_to_do:
    procesors_needed = processors_to_do - cpu_to_build
    profit = procesors_needed * 110.10
    print(f"Profit: -> {abs(profit):.2f} BGN")