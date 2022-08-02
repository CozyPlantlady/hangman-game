from logo import print_logo
from hangman import print_hangman, print_hangman_win
from guess import user_guess
from word import get_word

game_on = True
correct_answers = 0
wrong_answers = 0
guessed_letters = []


def game_loop():
    """
    Loops until user loses or wins
    """
    word = get_word()
    global correct_answers
    global wrong_answers
    print_logo()
    print_hangman(wrong_answers)
    while game_on is True:
        loop_this()
    if game_on is not True:
        if correct_answers == len(word):
            print_hangman_win()
            print("Congratulations! You WON!")
        if wrong_answers == 6:
            print(f"Sorry, you lost :( The word was {word}")
        print("Game has ended.")


def loop_this():
    """
    The loop that takes users answer, checks if it's correct or wrong,
    and gives points.
    """
    global correct_answers
    global wrong_answers
    global guessed_letters
    global game_on
    word = get_word()
    while wrong_answers < 6 and correct_answers < len(word):
        input_guess = user_guess()
        if input_guess in guessed_letters:
            print(f"You already guessed {input_guess}. Try again.\n")
        elif input_guess not in word:
            print(f"Sorry, {input_guess} is not in this word.")
            guessed_letters.append(input_guess)
            wrong_answers += 1
            print_hangman(wrong_answers)
            print(f"Used letters:\n{guessed_letters}\n")
            return guessed_letters, wrong_answers
        elif input_guess in word:
            print(f"Correct! {input_guess} is in the word!\n")
        for letter in word:
            if input_guess in letter:
                print(letter, end=" ")
                guessed_letters.append(input_guess)
                correct_answers += 1
            elif letter in guessed_letters and word:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print(f"\nUsed letters:\n{guessed_letters}\n")
    game_on = False
    return game_on
