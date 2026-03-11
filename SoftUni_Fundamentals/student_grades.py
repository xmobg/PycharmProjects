grades = list(map(int,input().split()))
good_students = 0
over_all_grades = 0
for grade in grades:
    if grade >= 5:
        good_students += 1
over_all_grades = sum(grades) / len(grades)
print(f"Брой отличници: {good_students}")
print(f"Средна оценка: {over_all_grades:.2f}")