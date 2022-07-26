from word import validate_word


def user_guess():
    """
    Getting the users answer
    """
    input_guess = input("Guess a letter:").upper()
    if input_guess.isalpha() is False:
        print(f"{input_guess} is not an alphabet.")
        user_guess()
    return input_guess


def print_word():
    """
    Takes values from user_guess and collect_guessed_letters
    to decide which letters to print.
    """
    right_answer = 0
    wrong_answer = 0
    word = validate_word()
    guessed_letters = []
    print(word)
    input_guess = user_guess()
    if input_guess in guessed_letters:
        print(f"You already guessed {input_guess}. Try again.")
    for letter in word:
        if input_guess in letter:
            print(letter, end=" ")
            guessed_letters.append(input_guess)
            right_answer += 1
        elif letter in guessed_letters and word:
            print(letter, end=" ")
        elif input_guess not in word:
            print(f"Sorry, {input_guess} is not in this word.")
            guessed_letters.append(input_guess)
            wrong_answer += 1
            print_hangman(wrong_answer)
        else:
            print("_", end=" ")
    print(f"\n Guessed letters:{guessed_letters}")
    return guessed_letters
