numbers_of_electons = int(input())
shells = []
number_of_shells = 0
while numbers_of_electons > 0:
    number_of_shells += 1
    max_electrons_in_current_shell = 2 * number_of_shells ** 2
    if numbers_of_electons >= max_electrons_in_current_shell:
        shells.append(max_electrons_in_current_shell)
    else:
        shells.append(numbers_of_electons)
    numbers_of_electons -= max_electrons_in_current_shell
print(shells)