GOAL_STEPS_DAY = 10000
sum_steps = 0

while sum_steps < GOAL_STEPS_DAY:
    current_steps = input()

    if current_steps == "Going home":
        steps_to_home = int(input())
        sum_steps += steps_to_home
        break

    sum_steps += int(current_steps)

if sum_steps >= GOAL_STEPS_DAY:
    print("Goal reached! Good job!")
    print(f"{sum_steps - GOAL_STEPS_DAY} steps over the goal!")
else:
    print(f"{GOAL_STEPS_DAY - sum_steps} more steps to reach goal.")
