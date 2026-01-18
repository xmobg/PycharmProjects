import random
lives = 6
word_list = ["bamboo", "banana","apple", "camel"]
logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
random_word = random.choice(word_list)
print(logo)
print(random_word)
placeholder = " "
word_len = len(random_word)
for position in range(word_len):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
while not game_over:
    guess = input("Guess a letter: ").lower()
    print(f"You have {lives} lives left")
    display = " "
    for letter in random_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)
    if guess not in random_word:
        lives -= 1
        if lives == 0:
            game_over = True
    if "_" not in display:
        game_over = True
        print("You win!")
    elif lives == 0 :
        print("You lose!")
        game_over = True