sequence = input().split()
moves = 0

while True:
    command = input()
    if command == "end":
        break

    moves += 1
    idx1, idx2 = map(int, command.split())


    if idx1 == idx2 or idx1 < 0 or idx2 < 0 or idx1 >= len(sequence) or idx2 >= len(sequence):
        middle = len(sequence) // 2
        new_element = f"-{moves}a"
        sequence.insert(middle, new_element)
        sequence.insert(middle, new_element)
        print("Invalid input! Adding additional elements to the board")
        continue


    element1 = sequence[idx1]
    element2 = sequence[idx2]

    if element1 == element2:
        print(f"Congrats! You have found matching elements - {element1}!")

        for i in sorted([idx1, idx2], reverse=True):
            sequence.pop(i)
    else:
        print("Try again!")


    if len(sequence) == 0:
        print(f"You have won in {moves} turns!")
        break


if sequence:
    print("Sorry you lose :(")
    print(" ".join(sequence))