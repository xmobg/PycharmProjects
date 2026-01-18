hour = int(input())
day_of_week = input()
working_days = ["Monday", "Tuesday", "Wednesday","Thursday","Friday","Saturday"]
if day_of_week in working_days and  18 > hour >= 10:
    print("open")
elif day_of_week in working_days and 18 < hour < 10:
    print("closed")

else:
    print("closed")