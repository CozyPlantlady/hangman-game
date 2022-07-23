import requests


get_word = requests.get("https://random-word-api.herokuapp.com/word?lang=en&length=6&number=1")

word = get_word.text.upper()


def user_guess(letter):
    """
    Getting the users guess
    """
    return input(letter)


guess = user_guess("Guess a letter:").upper()


wrong_answer = 0

print(word)
print(guess)

def show_word(word):
    for letter in word:
        print("_")
        if guess in letter:
            print(letter)

show_word(word)
