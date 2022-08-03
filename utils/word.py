import requests


def get_word_from_api():
    return requests.get(
    "https://random-word-api.herokuapp.com/word?lang=en&number=1"
    )


def get_word():
    """
    Gets the random word and removes symbols
    """
    new_word = get_word_from_api().text.upper()
    word = new_word.translate({ord(new_word): None for new_word in '[]"'})
    return word
