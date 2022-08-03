from utils.logo import print_logo
from utils.hangman import print_hangman, print_hangman_win
from utils.word import get_word
#from guess import user_guess

GAME_ON = True
CORRECT_ANSWERS = 0
WRONG_ANSWERS = 0
GUESSED_LETTERS = []

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

def game_loop():
    """
    Gets the random word, prints title and starts the loop_this function.
    Loops until user loses or wins
    """
    word = get_word()
    global CORRECT_ANSWERS
    global WRONG_ANSWERS
    print_logo()
    while GAME_ON is True:
        loop_this()
    if GAME_ON is not True:
        if WRONG_ANSWERS == 6:
            print(f"Sorry, you lost :( The word was {word}")
        else:
            print_hangman_win()
            print("Congratulations! You WON!")
        print("Thank you for playing! To replay, run program again <3")


def loop_this():
    """
    The loop that takes users answer, checks if it's correct or wrong,
    and gives points depending of outcome.
    """
    global CORRECT_ANSWERS
    global WRONG_ANSWERS
    global GUESSED_LETTERS
    global GAME_ON
    word = get_word()
    while WRONG_ANSWERS < 6 and CORRECT_ANSWERS < len(word):
        input_guess = user_guess()
        if input_guess not in word:
            print(f"Sorry, {input_guess} is not in this word.")
            GUESSED_LETTERS.append(input_guess)
            WRONG_ANSWERS += 1
            print_hangman(WRONG_ANSWERS)
            print(f"Used letters:\n{GUESSED_LETTERS}\n")
            return GUESSED_LETTERS, WRONG_ANSWERS
        elif input_guess in word:
            print(f"Correct! {input_guess} is in the word!\n")
        for letter in word:
            if input_guess in letter:
                print(letter, end=" ")
                GUESSED_LETTERS.append(input_guess)
                CORRECT_ANSWERS += 1
            elif letter in GUESSED_LETTERS and word:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print(f"\nUsed letters:\n{GUESSED_LETTERS}\n")
    GAME_ON = False
    return GAME_ON
