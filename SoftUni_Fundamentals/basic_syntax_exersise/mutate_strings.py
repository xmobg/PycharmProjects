first_string = input()
second_string = input()
for string_mutate in range(len(first_string)):
    left_part = second_string[:string_mutate+1:]
    right_part = first_string[string_mutate+1:]
    new_string = left_part + right_part
    if first_string[string_mutate] != second_string[string_mutate]:
        print(new_string)