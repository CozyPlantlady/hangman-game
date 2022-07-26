from word import validate_word


guessed_letters = []


def user_guess():
    """
    Getting the users answer
    """
    input_guess = input("Guess a letter:").upper()
    return input_guess


def print_word():
    """
    Takes values from user_guess and collect_guessed_letters
    to decide which letters to print.
    """
    word = validate_word()
    print(word)
    input_guess = user_guess()
    if input_guess in guessed_letters:
        print(f"You already guessed {input_guess}. Try again.")
    for letter in word:
        if input_guess in letter:
            print(letter, end=" ")
        elif input_guess in guessed_letters and word:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    guessed_letters.append(input_guess)
    print(f"\n Guessed letters:{guessed_letters}")
    return guessed_letters


guess = 0


while guess <= 10:
    guess += 1
    print_word()
