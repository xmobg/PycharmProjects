energy = float(input())
artefact_count = 0
artefact = 0
while True:
    action = input()
    if action == "Journey ends here!":
        break
    elif action == "mountain":
        energy -= 10
        artefact_count += 1
        if artefact_count % 3 == 0:
            artefact += 1
    elif action == "desert":
        energy -= 15
    elif action == "forest":
        energy += 7
    if energy <= 0:
        print("The character is too exhausted to carry on with the journey.")
        exit()
    if artefact == 3:
        print(f"The character reached the legendary artifact with {energy:.2f} energy left.")
        exit()
print(f"The character could not find all the pieces and needs {3-artefact} more to complete the legendary artifact.")
