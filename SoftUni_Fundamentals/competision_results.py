results = list(map(int,input().split()))
list_with_results_over_fifty = []
perfect_score = 0
for result in results:
    if result >= 50:
        list_with_results_over_fifty.append(result)


for result in list_with_results_over_fifty:
    if result >= 80:
        perfect_score += 1

print(f"Нов списък (мин. 50) в обратен ред: ",list_with_results_over_fifty[::-1])
print(f"Брой отличници (≥80): {perfect_score}")
print(f"Среден резултат на всички участници: {sum(results)/len(results):.2f}")
print(f"Обща сума на резултатите ≥50: {sum(list_with_results_over_fifty)}")