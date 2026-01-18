from math import ceil
persons_for_elevator = int(input())
elevator_capacity = int(input())
courses_needed = ceil(persons_for_elevator/elevator_capacity)
print(courses_needed)