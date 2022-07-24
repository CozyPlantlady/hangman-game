import requests


get_word = requests.get("https://random-word-api.herokuapp.com/word?lang=en&length=6&number=1")


new_word = get_word.text.upper()
word = new_word.translate({ord(new_word): None for new_word in '[]"'})


print(word)
