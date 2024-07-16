# -------------------------
def new_game():

    guesses = []
    correct_guesses = 0
    questions_num = 1

    for key in questions:
        print("------------------------")
        print(key)
        for i in options[questions_num-1]:
            print(i)
        guess = input("Enter your answer (A, B, C, D, or E): ")
        guess = guess.upper()

        while guess not in ['A', 'B', 'C', 'D', 'E']:
            guess = input("Invalid input. Please enter your answer (A, B, C, D, or E): ")
            guess = guess.upper()

        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        questions_num += 1

    display_score(correct_guesses, guesses)

# -------------------------


def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# -------------------------


def display_score(correct_guesses, guesses):
    print("------------------------")
    print("RESULTS")
    print("------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is "+str(score)+"%")

# -------------------------


def play_again():
    response = input("Do you wanna play again? (yes/no): ")
    response = response.lower()

    while response not in ['yes', 'no']:
        response = input("Invalid input. Do you wanna play again? (yes/no): ")
        response = response.lower()

    if response == "yes":
        return True
    else:
        return False

# -------------------------


questions = {
    "Who was the first president of Indonesia? ": "A",
    "When did Indonesia gain their independence? ": "D",
    "Where did the author of this game go to school? ": "A",
    "What is the name of the capital ciy of Riau province? ": "B"
}

options = [
    ["A. Soekarno", "B. Soekarni", "C. Moh. Hatta", "D. Jokowi", "E. BJ. Habibie"],
    ["A. 1990", "B. 2011", "C. 1951", "D. 1945", "E. 1975"],
    ["A. Al-Ittihad", "B. Cendana", "C. Dharma Yuda", "D. Santa Maria", "E. Al-Bayinnah"],
    ["A. Jakarta", "B. Pekanbaru", "C. Medan", "D. Malang", "E. Bali"],
]

new_game()

while play_again():
    new_game()

print("Goodbye!")
