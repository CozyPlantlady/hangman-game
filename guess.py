def user_guess():
    """
    Getting the users answer
    """
    input_guess = input("\nGuess a letter:").upper()
    if input_guess.isalpha() is False:
        print(f"{input_guess} is not an alphabet.")
        user_guess()
    elif len(input_guess) != 1:
        print("Please give a single letter.")
        user_guess()
    else:  # len(input_guess) == 1 and input_guess.isalpha() is True:
        return input_guess
