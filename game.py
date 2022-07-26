from logo import print_logo
from hangman import print_hangman
from guess import user_guess
from word import validate_word

guessed_letters = user_guess()
word = validate_word()


def game():
    """
    Main game loop gets functions from other files, and prints the hangman if user answers wrong
    """
    wrong_answers = 0
    print_logo()
    while wrong_answers <= 6:
        user_guess()
        if guessed_letters not in word:
            wrong_answers += 1
            print_hangman(wrong_answers)
       

game()