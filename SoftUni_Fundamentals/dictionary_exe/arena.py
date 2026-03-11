arena = {}

while True:
    command = input()
    if command == "end":
        break
    player,position,skill = command.split(" -> ")
    skill = int(skill)
    if player not in arena:
        arena[player] = {}
    if position not in arena[player] or arena[player][position] < skill:
        arena[player][position] = skill

for player, positions in arena.items():
    print(player)
    for pos, skill in positions.items():
        print(f"- {pos} <::> {skill}")