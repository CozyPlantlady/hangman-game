from utils.logo import print_logo
from utils.hangman import print_hangman, print_hangman_win
from utils.word import get_word


GAME_ON = True
CORRECT_ANSWERS = 0
WRONG_ANSWERS = 0
GUESSED_LETTERS = []
WORD = get_word()

def user_guess():
    """
    Getting the user input. Turns users answer to uppercase to match
    the random word. Gives error message if user gives too long input or
    uses non-alphabets.
    Loops until it gets valid answer.
    """
    global GUESSED_LETTERS
    valid_answer = False

    while valid_answer is False:
        try:
            input_guess = input("\nGuess a letter:\n").upper()
            if input_guess.isalpha() is False:
                raise ValueError(f"{input_guess} is not an alphabet.")

            if len(input_guess) != 1:
                raise ValueError("Please give a single letter.")

            if input_guess in GUESSED_LETTERS:
                raise ValueError("You have already guessed this letter.")

            if len(input_guess) == 1 and input_guess.isalpha() is True:
                valid_answer = True
                return input_guess

        except ValueError as error:
            print(f"{error} Let's try again.")


def status_quo():
    """
    Clears the global variables after user have chosen to replay.
    Fetches a new random word for the new game
    """
    global GAME_ON
    GAME_ON = True
    global CORRECT_ANSWERS
    CORRECT_ANSWERS = 0
    global WRONG_ANSWERS
    WRONG_ANSWERS = 0
    global GUESSED_LETTERS
    GUESSED_LETTERS = []
    global WORD
    WORD = get_word()
    game_loop()


def game_loop():
    """
    Gets the random word, prints title and starts the loop_this function.
    Loops until user loses or wins.
    """
    global WORD
    global CORRECT_ANSWERS
    global WRONG_ANSWERS

    print_logo()

    while GAME_ON is True:
        loop_this()

    if GAME_ON is not True:
        if WRONG_ANSWERS == 7:
            print(f"Sorry, you lost :( The word was {WORD}")
        else:
            print_hangman_win()
            print("Congratulations! You WON!")

        lets_continue = input("\nDo you want to play again? Y/N:\n").upper()

        if lets_continue == "Y":
            status_quo()
        else:
            print("Thank you for playing!")


def loop_this():
    """
    The loop that takes users answer, checks if it's correct or wrong,
    and gives points depending of outcome.
    """
    global CORRECT_ANSWERS
    global WRONG_ANSWERS
    global GUESSED_LETTERS
    global GAME_ON
    global WORD

    while WRONG_ANSWERS < 7 and CORRECT_ANSWERS < len(WORD):
        input_guess = user_guess()

        if input_guess not in WORD:
            print(f"Sorry, {input_guess} is not in this word.")
            GUESSED_LETTERS.append(input_guess)
            WRONG_ANSWERS += 1
            print_hangman(WRONG_ANSWERS)
            print(f"Used letters:\n{GUESSED_LETTERS}\n")
            return GUESSED_LETTERS, WRONG_ANSWERS

        if input_guess in WORD:
            print(f"Correct! {input_guess} is in the word!\n")

        for letter in WORD:
            if input_guess in letter:
                print(letter, end=" ")
                GUESSED_LETTERS.append(input_guess)
                CORRECT_ANSWERS += 1

            elif letter in GUESSED_LETTERS and WORD:
                print(letter, end=" ")

            else:
                print("_", end=" ")

        print(f"\nUsed letters:\n{GUESSED_LETTERS}\n")

    GAME_ON = False
    return GAME_ON
