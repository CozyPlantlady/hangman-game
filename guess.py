from word import validate_word

guessed_letters = []
word = validate_word()


def user_guess():
    """
    Getting the users answer and adding it to guessed letters list
    """
    print(word) """For testing"""
    guessed_letter = input("Guess a letter:").upper()
    for letter in word:
        if guessed_letter in letter:
            print(letter, end=" ")
        elif guessed_letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    guessed_letters.append(guessed_letter)
    print(f"\n Guessed letters:{guessed_letters}")
    return guessed_letters
