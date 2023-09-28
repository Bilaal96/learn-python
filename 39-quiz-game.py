# 39 (03:18:32​) quiz game 💯
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    # Print question, answer options, and prompt for user answer
    for question in questions:
        print("-----------------------")
        print(question)
        for option in options[question_num-1]:
            print(option)
        
        # Record user answers
        guess = input("Enter (A, B, C, or D): ").upper()
        guesses.append(guess)

        # Check user answer
        # NOTE: remember Dict.get() accesses non-existent keys safely (without error)
        # questions.get(question) returns the correct answer
        correct_guesses += check_answer(questions.get(question), guess) 

        # Increment question_num to get options for the next question
        question_num += 1

    # print score
    display_score(correct_guesses, guesses)

# ---------------------------------------------------------------------------- #
def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1 # point
    else:
        print("WRONG!")
        return 0 # no point

# ---------------------------------------------------------------------------- #
def display_score(correct_guesses, guesses):
    print("-----------------------")
    print("RESULTS")
    print("-----------------------")
    # Print answers
    print("Answers: ", end="")
    for q in questions:
        print(questions.get(q), end=" ")
    print()
    # Print guesses
    print("Guesses: ", end="")
    for g in guesses:
        print(g, end=" ")
    print()

    # cast from float to int to remove decimal places 
    score = int(correct_guesses / len(questions) * 100)
    print("Your score is: "+str(score) + "%")

# ---------------------------------------------------------------------------- #
def play_again():
    response = input("Do you want to play again (y/n)?: ").lower()
    if response == "y": 
        return True
    else:
        return False

# ---------------------------------------------------------------------------- #

# Value holds answer
questions = {
    "Who created Python?": "A",
    "What year was Python created?": "B",
    "Python is tributed to which comedy group": "C",
    "Is the Earth round?": "A"
}

# 2D list of possible answers
options = [
    ["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
    ["A. True", "B. False", "C. Sometimes", "D. What's Earth?"],
]

new_game()

while play_again(): 
    new_game()

print("Thanks for playing!")