import time

rounds_to_fight = 3
time_of_rounds = 5
rest_time = 3

def format_time(seconds: int):
    return f"{seconds // 60:02d}:{seconds % 60:02d}"

def round_timer(round_number: int, duration: int):
    print(f"\nRound {round_number} started!")
    for timer_count in range(duration, 0, -1):
        print(f"Time left: {format_time(timer_count)}  ")
        time.sleep(1)
    print(f"Round {round_number} ended!\a")  # beep при край на рунд

def rest_timer(duration: int):
    print(f"Rest started!")
    for rest_count in range(duration, 0, -1):
        print(f"Rest time left: {format_time(rest_count)}")
        time.sleep(1)
    print("Rest ended!\a")  # beep при край на почивката

def start_fight(rounds, round_time, rest_time):
    for round_number in range(1, rounds + 1):
        round_timer(round_number, round_time)
        if round_number != rounds:
            rest_timer(rest_time)
    print("Fight is over!\a")

start_fight(rounds_to_fight, time_of_rounds, rest_time)
