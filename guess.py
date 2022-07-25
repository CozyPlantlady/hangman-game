from word import validate_word


guessed_letters = []
word = validate_word()


def user_guess():
    """
    Getting the users answer
    """
    input_guess = input("Guess a letter:").upper()
    return input_guess


def collect_guessed_letters():
    """
    Collects letters user has guessed
    """
    ### Needs to get input_guess value correctly
    guessed_letters.append(input_guess)
    print(f"\n Guessed letters:{guessed_letters}")
    print(guessed_letters)
    return guessed_letters


def print_word():
    """
    Takes values from user_guess and collect_guessed_letters
    to decide which letters to print.
    """
    user_guess()
    collect_guessed_letters()
    for letter in word:
        if input_guess in letter:
            print(letter, end=" ")
        elif input_guess in guessed_letters:
            print("You already guessed {input_guess}. Try again.")
        elif guessed_letters in letter:
            print(letter, end=" ")
        else:
            print("_", end=" ")


guess = 0


while guess <= 10:
    guess += 1
    user_guess()
    collect_guessed_letters()
