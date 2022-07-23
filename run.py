import requests

get_word = requests.get("https://random-word-api.herokuapp.com/word?lang=en&length=6&number=1")

word = get_word.text.upper()
print(word)

guess_this_word = ()

