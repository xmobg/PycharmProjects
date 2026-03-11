def filter_len(word_len,list_of_elements):
    new_list = []
    for element in list_of_elements:
        if word_len < len(element):
            new_list.append(element)
    return new_list


words = ["cat", "elephant", "sun", "dictionary"]

lenght_of_word = int(input())
print(filter_len(lenght_of_word, words))