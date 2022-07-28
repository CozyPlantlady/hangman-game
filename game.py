from logo import print_logo
from hangman import print_hangman
from guess import user_guess
from word import validate_word

game_on = True
correct_answers = 0
wrong_answers = 0


def game_loop():
    """
    Loops until user loses or wins
    """
    word = validate_word()
    global correct_answers
    global wrong_answers
    print_logo()
    print(word)
    print_hangman(wrong_answers)
    while game_on is True:
        loop_this()
    if game_on is not True:
        if correct_answers == len(word):
            print("Congratulations! You WON!")
        if wrong_answers == 6:
            print("Sorry, you lost :(")
        print("Ooops")


def loop_this():
    """
    The loop that takes users answer, checks if it's correct or wrong,
    and gives points.
    """
    global correct_answers
    global wrong_answers
    guessed_letters = []
    word = validate_word()
    while wrong_answers < 6 and correct_answers < len(word):
        input_guess = user_guess()
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
                    correct_answers += 1
                    return correct_answers
                if letter in guessed_letters and word:
                    print(letter, end=" ")
                else:
                    print("_", end=" ")
                    print(f"\n Guessed letters:{guessed_letters}")
                    return guessed_letters   
    global game_on
    game_on = False
    return game_on
