arena = {}

while True:
    command = input()
    if command == "Season end":
        break

    if "->" in command:

        player, position, skill = command.split(" -> ")
        skill = int(skill)
        if player not in arena:
            arena[player] = {}
        if position not in arena[player] or arena[player][position] < skill:
            arena[player][position] = skill

    elif "vs" in command:

        player1, player2 = command.split(" vs ")

        if player1 in arena and player2 in arena:

            common = any(pos in arena[player2] for pos in arena[player1])
            if common:
                total_skill1 = sum(arena[player1].values())
                total_skill2 = sum(arena[player2].values())
                if total_skill1 > total_skill2:
                    del arena[player2]
                elif total_skill2 > total_skill1:
                    del arena[player1]


sorted_arena = sorted(arena.items(), key=lambda x: (-sum(x[1].values()), x[0]))

for player, positions in sorted_arena:
    total_skill = sum(positions.values())
    print(f"{player}: {total_skill} skill")

    sorted_positions = sorted(positions.items(), key=lambda x: (-x[1], x[0]))
    for pos, skill in sorted_positions:
        print(f"- {pos} <::> {skill}")