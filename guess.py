def user_guess():
    """
    Getting the users answer
    """
    input_guess = input("\nGuess a letter:").upper()
    if input_guess.isalpha() is False:
        print(f"{input_guess} is not an alphabet.")
        input_guess = input("\nGuess a letter:").upper()
    if len(input_guess) != 1:
        print("Please give a single letter.")
        print(type(input_guess))
        print(input_guess)
        input_guess = input("\nGuess a letter:").upper()
    if len(input_guess) == 1 and input_guess.isalpha() is True:
        return input_guess
    print("Something went wrong. Let's try again.")
    user_guess()
