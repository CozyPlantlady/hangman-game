def print_hangman(wrong_answers):
    """
    Prints the hanged man depending on how many times user have guessed wrong
    """
    if wrong_answers == 1:
        print("\n||======")
        print("||//")
        print("||/")
        print("||")
        print("||")
        print("||")
        print("||")
        print("||...........................................\n")
    elif wrong_answers == 2:
        print("\n||======")
        print("||//   |")
        print("||/    |")
        print("||     o")
        print("||")
        print("||")
        print("||")
        print("||...........................................\n")
    elif wrong_answers == 3:
        print("\n||======")
        print("||//   |")
        print("||/    |")
        print("||     o")
        print("||     |")
        print("||")
        print("||")
        print("||...........................................\n")
    elif wrong_answers == 4:
        print("\n||======")
        print("||//   |")
        print("||/    |")
        print("||     o")
        print("||    /|")
        print("||")
        print("||")
        print("||...........................................\n")
    elif wrong_answers == 5:
        print("\n||======")
        print("||//   |")
        print("||/    |")
        print("||     o")
        print("||    /|\\")
        print("||")
        print("||")
        print("||...........................................\n")
    elif wrong_answers == 6:
        print("\n||======")
        print("||//   |")
        print("||/    |")
        print("||     o")
        print("||    /|\\")
        print("||    /")
        print("||")
        print("||...........................................\n")
    elif wrong_answers == 7:
        print("\n||======")
        print("||//   |")
        print("||/    |")
        print("||     o")
        print("||    /|\\")
        print("||    / \\")
        print("||")
        print("||.......GAME OVER...........................\n")
    else:
        print("?")


def print_hangman_win():
    """
    Picture that will be printed if user wins the game.
    """
    print("\n||======")
    print("||//")
    print("||/")
    print("||                             YOU WON!!!")
    print("||")
    print("||                                 \\o/")
    print("||                                  |")
    print("||................................./.\\.......\n")
