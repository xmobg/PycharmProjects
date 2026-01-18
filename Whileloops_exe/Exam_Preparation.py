allowed_bad_grades = int(input())
sum_grades = 0
number_solver_problems = 0
number_bad_grades = 0
last_task = ""
is_enough = False

while allowed_bad_grades > number_bad_grades:
    task_name = input()

    if task_name == "Enough":
        is_enough = True
        break

    grade = int(input())
    if grade <= 4:
        number_bad_grades +=1

    sum_grades += grade
    number_solver_problems += 1
    last_task = task_name

if is_enough:
        print(f"Average score: {sum_grades / number_solver_problems:.2f}")
        print(f"Number of problems: {number_solver_problems}")
        print(f"Last problem: {last_task}")
else:
        print(f"You need a break, {number_bad_grades} poor grades.")
