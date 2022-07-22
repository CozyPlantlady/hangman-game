import requests

word = requests.get("https://random-word-api.herokuapp.com/word?lang=en&length=6&number=5")
print(word.text)