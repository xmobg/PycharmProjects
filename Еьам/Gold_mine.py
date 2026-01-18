
num_locations = int(input())

for _ in range(num_locations):
    expected_avg = float(input())
    days = int(input())

    total_gold = 0.0
    for _ in range(days):
        daily_gold = float(input())
        total_gold += daily_gold

    actual_avg = total_gold / days

    if actual_avg >= expected_avg:
        print(f"Good job! Average gold per day: {actual_avg:.2f}.")
    else:
        diff = expected_avg - actual_avg
        print(f"You need {diff:.2f} gold.")