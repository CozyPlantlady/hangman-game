from logo import print_logo
from hangman import print_hangman
from guess import user_guess
from word import validate_word


word = validate_word()
guessed_letters = []
correct_answers = 0
wrong_answers = 0


def get_point(answer):
    """
    Collects number of correct answers
    """
    points = answer
    points += 1
    print(f"answer is {points}")
    return points


def game_loop():
    """
    Loops until user loses or wins
    """
    game_on = True
    print_logo()
    print(word)
    while game_on is True:
        loop_this()
    if correct_answers == len(word):
        print("Congratulations! You WON!")
        game_on = False
        return game_on
    if wrong_answers == 6:
        print("Sorry, you lost :(")
        game_on = False
        return game_on
    print("Ooops")
    game_on = False
    return game_on


def loop_this():
    """
    The loop that takes users answer, checks if it's correct or wrong,
    and gives points.
    """
    input_guess = user_guess()
    if input_guess in guessed_letters:
        print(f"You already guessed {input_guess}. Try again.")
    elif input_guess not in word:
        print(f"Sorry, {input_guess} is not in this word.")
        guessed_letters.append(input_guess)
        get_point(wrong_answers)
        print_hangman(wrong_answers)
        print(f"\n Guessed letters:{guessed_letters}")
        return guessed_letters
    elif input_guess in word:
        for letter in word:
            if input_guess in letter:
                print(letter, end=" ")
                guessed_letters.append(input_guess)
                get_point(correct_answers)
            if letter in guessed_letters and word:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print(f"\n Guessed letters:{guessed_letters}")
        return guessed_letters
    else:
        print("huh. Thats weird.")
        game_on = False
        return game_on
