wrong_answer = 6


def print_hangman(wrong_answer):
    """
    Prints the hanged man depending on how many times user have guessed wrong
    """
    if wrong_answer == 0:
        print("||======")
        print("||//   |")
        print("||/    |")
        print("||")
        print("||")
        print("||")
        print("||")
        print("||.......")
    elif wrong_answer == 1:
        print("||======")
        print("||//   |")
        print("||/    |")
        print("||     o")
        print("||")
        print("||")
        print("||")
        print("||.......")
    elif wrong_answer == 2:
        print("||======")
        print("||//   |")
        print("||/    |")
        print("||     o")
        print("||     |")
        print("||")
        print("||")
        print("||.......")
    elif wrong_answer == 3:
        print("||======")
        print("||//   |")
        print("||/    |")
        print("||     o")
        print("||    /|")
        print("||")
        print("||")
        print("||.......")
    elif wrong_answer == 4:
        print("||======")
        print("||//   |")
        print("||/    |")
        print("||     o")
        print("||    /|\\")
        print("||")
        print("||")
        print("||.......")
    elif wrong_answer == 5:
        print("||======")
        print("||//   |")
        print("||/    |")
        print("||     o")
        print("||    /|\\")
        print("||    /")
        print("||")
        print("||.......")
    elif wrong_answer == 6:
        print("||======")
        print("||//   |")
        print("||/    |")
        print("||     o")
        print("||    /|\\")
        print("||    / \\")
        print("||")
        print("||.......GAME OVER")
    else:
        print("?")
        