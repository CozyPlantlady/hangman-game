def user_guess():
    """
    Getting the user input. Turns users answer to uppercase to match the random word.
    Gives error message if user gives too long input or uses non-alphabets.
    Loops until valid answer is given.
    """
    valid_answer = False
    while valid_answer is False:
        try:
            input_guess = input("\nGuess a letter:\n").upper()
            if input_guess.isalpha() is False:
                raise ValueError(f"{input_guess} is not an alphabet.")
            if len(input_guess) != 1:
                raise ValueError("Please give a single letter.")
            if len(input_guess) == 1 and input_guess.isalpha() is True:
                valid_answer = True
                return input_guess
        except ValueError as error:
            print(f"{error} Let's try again.")
