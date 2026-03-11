players_result = list(map(int, input().split()))
score_over_eighty = 0
for player in players_result:
    if player > 80:
        score_over_eighty += 1
score_avarage = sum(players_result) / len(players_result)
print(f"Най-висок резултат: {max(players_result)}")
print(f"Брой играчи над 80: {score_over_eighty}")
print(f"Среден резултат: {score_avarage:.2f}")
