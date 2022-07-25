# Hangman game


## Strategy
Hangman is a classic word-guessing game, where user has to guess the right word. If user guesses wrong six times, it's game over.
If user guesses right they win. This game is suitable for anyone who understands english language. User will most likely wish to challenge themselves, and be entertained.

## Scope
Game lets the user to guess untill they get the word right, or until they guess wrong six times. Game is unlimitedly replayable, as long as there is words left.

### User goals:
What is their goal? What problem does this product or feature solve for them?
- It's a game, and user wants to be challenged and entertained.

### User Stories:
- As a user I can start the game.
- As a user I can find more information about how to play the game.
- As a user I can guess a letter.
- As a user I can choose to replay.

## Structure and skeleton

### Structure of the game
Original plan for the game

![](doc/readme-images/readme-wireframe.png "")

Welcome:
When game is started, it first greets the user with logo, and option to start the game right away or read the rules first.

Rules:

The game:
The main game loop lets user to input a letter. If the letter is in the word, it is shown in the  letter field in correct spot. 
If letter is incorrect, it's added to the used letters list, and user loses a point.
Game continues until all the letters in a word are guessed and word is revealed, or until user guesses wrong six times.

Replay:
User can replay by choosing "Yes".
If user chooses "No", it takes them to the start screen.

## Skeleton:

## Surface:


## TESTING

### As a user I can start the game.
### As a user I can find more information about how to play the game.
### As a user I can guess a letter.
### As a user I can choose to replay.### Bugs and other issues:


### Fixed Issues
- Word prints down as a column. FIX: add **end=" "** to print statement to make it a row.
- When turning letters of the word to underscore, word_to_blank function returns 10 character instead of 6. Is it counting "" and []-characters? The extra symbols are coming from the API. 
Like this:

![](doc/readme-images/readme-glitch1.png "") 

FIX: added code to remove unwanted letters/symbols from the random word.
- Creating a infinite loop when guessing a letter. 

### Not fixed
- Only showing the first correctly guessed letter
- Showing the whole word when guessing a letter
- Printing error message 6 times (once for each letter)
- Adding same letter to the guessed letters list

### Testing with code validators


### DEPLOYMENT
- Site was deployed to **Github Pages**.
- From Github, I chose the current project **Hangman-game** and **Settings**.
- On the leftside of the page there is **Pages**.
- Choose the **Main** branch
- Site will be published.
- This site is published at:


## CREDITS

Code:
- [To remove extra symbols from random word](https://www.journaldev.com/23674/python-remove-character-from-string)
s = 'abc12321cba'

print(s.translate({ord(i): None for i in 'abc'}))



### Validators:

### Other things I used while coding this game:

Balsamiq wireframes

[Text to ASCII generator](https://patorjk.com/software/taag)


