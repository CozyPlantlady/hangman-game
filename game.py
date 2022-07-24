from logo import print_logo
from hangman import print_hangman
from guess import user_guess

def game():
    """
    Main game loop
    """
    wrong_answer = 0
    guessed_letter = ""
    print_logo()
    while wrong_answer <= 6:
        user_guess()
        show_word(word)
        print(word)
        if guess not in word:
            wrong_answer += 1
            print_hangman(wrong_answer)
        elif guess in guessed_letters:
            print("You already guessed {guessed_letter}. Try again.")
        else:
            print("Right!")


game()