def calculate_love_score(name1, name2):
    true_total = 0
    love_total = 0
    for char in name1.lower():
        if char == "t":
            true_total += 1
        elif char == "r":
            true_total += 1
        elif char == "u":
            true_total += 1
        elif char == "e":
            true_total += 1
    for char in name2.lower():
        if char == "t":
            true_total += 1
        elif char == "r":
            true_total += 1
        elif char == "u":
            true_total += 1
        elif char == "e":
            true_total += 1
    for char in name1.lower():
        if char == "l":
            love_total += 1
        elif char == "o":
            love_total += 1
        elif char == "v":
            love_total += 1
        elif char == "e":
            love_total += 1
    for char in name2.lower():
        if char == "l":
            love_total += 1
        elif char == "o":
            love_total += 1
        elif char == "v":
            love_total += 1
        elif char == "e":
            love_total += 1
    love_score = str(true_total) + str(love_total)
    print(love_score)
calculate_love_score("Kanye West", "Kim Kardashian")
