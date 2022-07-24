import requests
from logo import print_logo
from hangman import print_hangman

get_word = requests.get("https://random-word-api.herokuapp.com/word?lang=en&length=6&number=1")

word = get_word.text.upper()

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


def game_start():
    """
    Start screen
    """
    print_logo()
    print("Welcome!\n")
    #print("Start the game or read the rules?\nS for START and R for RULES")
    #user_input = input("S or R:")
    #if user_input.upper == "S":
    game()
    #elif user_input.upper == "R":
    #    rules()
    #else:
    #    print("Please give a valid answer.")


def rules():
    print("These are the rules for the hangman game")
    game()


def game():
    while wrong_answer <= 6:
        user_guess()
        show_word(word)
        print(word)
        if guess not in word:
            wrong_answer += 1
            print_hangman(wrong_answer)
        elif guess in guessed_letters:
            print("You already guessed {guessed_letter}. Try again.")
        else:
            print("Right!")

game_start()