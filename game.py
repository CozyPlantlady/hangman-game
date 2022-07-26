from logo import print_logo
from hangman import print_hangman
from guess import user_guess
from word import validate_word


def game():
    """
    Takes values from user_guess and collect_guessed_letters
    to decide which letters to print.
    """
    game_on = True
    word = validate_word()
    guessed_letters = []
    print_logo()
    print(word)
    input_guess = user_guess()
    right_answers = 0
    wrong_answers = 0
    while game_on is True:
        if input_guess in guessed_letters:
            print(f"You already guessed {input_guess}. Try again.")
        elif input_guess not in word:
            print(f"Sorry, {input_guess} is not in this word.")
            guessed_letters.append(input_guess)
            wrong_answers += 1
            print_hangman(wrong_answers)
            print(f"\n Guessed letters:{guessed_letters}")
            return guessed_letters
        elif input_guess in word:
            for letter in word:
                if input_guess in letter:
                    print(letter, end=" ")
                    guessed_letters.append(input_guess)
                    right_answers += 1
                elif letter in guessed_letters and word:
                    print(letter, end=" ")
                else:
                    print("_", end=" ")
            print(f"\n Guessed letters:{guessed_letters}")
            return guessed_letters
        else:
            print("huh. Thats weird.")
    if right_answers == len(word):
        print("Congratulations! You WON!")
        game_on = False
    elif wrong_answers == 6:
        print("Sorry, you lost :(")
        game_on = False
    else:
        print("Ooops")
