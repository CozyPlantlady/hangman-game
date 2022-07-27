from logo import print_logo
from hangman import print_hangman
from guess import user_guess
from word import validate_word


word = validate_word()
guessed_letters = []


def game_loop():
    """
    Loops until user loses or wins
    """
    right_answers = 0
    wrong_answers = 0
    input_guess = user_guess()
    print(word)
    if input_guess in guessed_letters:
        print(f"You already guessed {input_guess}. Try again.")
    elif input_guess not in word:
        print(f"Sorry, {input_guess} is not in this word.")
        guessed_letters.append(input_guess)
        wrong_answers += 1
        print_hangman(wrong_answers)
        print(f"\n Guessed letters:{guessed_letters}")
        return guessed_letters, wrong_answers
    elif input_guess in word:
        for letter in word:
            if input_guess in letter:
                print(letter, end=" ")
                guessed_letters.append(input_guess)
                right_answers += 1
                return right_answers
            if letter in guessed_letters and word:
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
        return game_on
    if wrong_answers == 6:
        print("Sorry, you lost :(")
        game_on = False
        return game_on
    else:
        print("Ooops")


def main_game():
    """
    Holds the game
    """
    game_on = True
    print_logo()
    while game_on is True:
        game_loop()
