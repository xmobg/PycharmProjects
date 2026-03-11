player_points = {}

while True:
    command = input()
    if command == "end":
        break
    player,points = command.split()
    points = int(points)
    if player not in player_points:
        player_points[player] = points
    else:
        player_points[player] += points

for player,points in player_points.items():
    print(f"{player} -> {points}")