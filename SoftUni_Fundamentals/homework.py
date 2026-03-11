items = [1, 2, 2, 3, 4, 4, 4, 5]

seen = set()
dupes = set()

for x in items:
    if x in seen:
        dupes.add(x)
    else:
        seen.add(x)

print(dupes, sep= ", ")