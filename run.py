import requests

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


while wrong_answer <= 6:
    user_guess()
    show_word(word)
    print(word)
    if guess not in word:
        wrong_answer += 1
    elif guess in guessed_letters:
        print("You already guessed {guess}. Try again.")
    else:
        print("Right!")
