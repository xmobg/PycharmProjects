employee_one = int(input())
employee_two = int(input())
employee_three = int(input())
students_count = int(input())
employee_total = employee_one + employee_two + employee_three
hours = 0
while students_count > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    students_count -= employee_total
print(f"Time needed: {hours}h.")