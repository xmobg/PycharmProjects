questions = ("What is the capital of France?: ",
             "Who wrote the novel '1984'?: ",
             "What is the largest ocean on Earth?: ",
             "How many continents are there?: ",
             "What is the square root of 64?: ")

options = (("A. Berlin", "B. Madrid", "C. Paris", "D. Rome"),
           ("A. George Orwell", "B. Ernest Hemingway", "C. F. Scott Fitzgerald", "D. J.K. Rowling"),
           ("A. Atlantic Ocean", "B. Indian Ocean", "C. Pacific Ocean", "D. Arctic Ocean"),
           ("A. 5", "B. 6", "C. 7", "D. 8"),
           ("A. 6", "B. 7", "C. 8", "D. 9"))

answers = ("C", "A", "C", "C", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A B C D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("---------------------------")
print("----------RESULTS----------")
print("---------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")