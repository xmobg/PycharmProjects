from math import floor
days = int(input())
days_off = days * 127
working_days = (365 - days) * 63
total_hours = working_days + days_off
play_time = abs((working_days + days_off) - 30000)
hours = (play_time // 60)
minutes = (play_time % 60)
if total_hours < 30000:
    print("Tom sleeps well")
    print(format(f"{hours} hours and {minutes} minutes less for play"))
elif total_hours > 30000:
    print("Tom will run away")
    print(format(f"{hours} hours and {minutes} minutes more for play"))