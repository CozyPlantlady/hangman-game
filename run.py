import requests

get_word = requests.get("https://random-word-api.herokuapp.com/word?lang=en&length=6&number=1")

word = get_word.text.upper()

def user_guess(letter):
    return input(letter)


guess = user_guess("Guess a letter:").upper()

for letter in word:
    if guess in word:
        print("right!")
    else:
        print("wrong.")


print(word)
