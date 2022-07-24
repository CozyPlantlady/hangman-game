
from logo import print_logo
from hangman import print_hangman



#guessed_letters = []
#guessed_letter = ""

#wrong_answer = 0


#def user_guess():
#    """
#    Getting the users answer and adding it to guessed letters list
#    """
#    guessed_letter = input("Guess a letter:").upper()
#    guessed_letters.append(guessed_letter)
#    print(f"Guessed letters:{guessed_letters}")
#    return guessed_letter


#guess = user_guess()


#def show_word(word):
#    """
#    Printing a letter or blank
#    """
#    for letter in word:
#        if guess in letter:
#            print(guess, end=" ")
#        else:
#            print("_", end=" ")


#def game_start():
#    """
#   Start screen
#    """
#    print_logo()
#    print("Welcome!\n")
#    game()


#def game():
#    while wrong_answer <= 6:
#        user_guess()
#        show_word(word)
#        print(word)
#        if guess not in word:
#            wrong_answer += 1
#            print_hangman(wrong_answer)
#        elif guess in guessed_letters:
#            print("You already guessed {guessed_letter}. Try again.")
#        else:
#            print("Right!")


game()
