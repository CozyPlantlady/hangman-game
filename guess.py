def user_guess():
    """
    Getting the users answer
    """
    input_guess = input("Guess a letter:").upper()
    if input_guess.isalpha() is False:
        print(f"{input_guess} is not an alphabet.")
        user_guess()
    if len(input_guess) != 1:
        print("Please give a single letter.")
    else:
        return input_guess
