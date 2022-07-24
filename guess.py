from word import validate_word


guessed_letters = []


guessed_letter = ""


wrong_answer = 0


def user_guess():
    """
    Getting the users answer and adding it to guessed letters list
    """
    guessed_letter = input("Guess a letter:").upper()
    guessed_letters.append(guessed_letter)
    print(f"Guessed letters:{guessed_letters}")
    return guessed_letter


guess = user_guess()


def show_word(word):
    """
    Printing a letter or blank
    """
    for letter in word:
        if guess in letter:
            print(guess, end=" ")
        else:
            print("_", end=" ")


