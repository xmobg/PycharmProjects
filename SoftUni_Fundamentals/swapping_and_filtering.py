results = list(map(int, input().split()))
new_results = []
over_eighty = 0
for result in results:
    if result >= 50:
        new_results.append(result)
    if result > 80:
        over_eighty += 1
print(new_results[::-1])
print(f"Брой резултати над 80: {over_eighty}")

