# Hangman game
When I was in school, we used to play hangman on the classrooms chalkboard. It was exciting to try to guess, while the poor stick figure man was getting drawn... It's easy to learn, but hard enough to keep you entertained! So for my third project I'll make a hangman game you can play for your own fun.

## Strategy
**Hangman** is a classic word-guessing game, where user has to guess the right word. If user guesses wrong, the stick character gets another part drawn. When user has guessed wrong six times, it's game over. If user guesses all the letters right they win. 
This game is suitable for anyone who understands english language, but its very easily translated to other languages that use latin-script alphabet. By changing the wordlist or API the game can be fit to different themes. I have chosen to use random word API with random letter length, but this too is easily customisable. I decide against letting user choose the letter length or difficulty in this project, since I want the game to start right away. Too many options are not always good. 
User will most likely wish to challenge themselves, and be entertained.

## Scope
Game lets the user guess untill they get the word right, or until they guess wrong six times. Game is unlimitedly replayable, as long as there is words left.

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
### As a user I can choose to replay.


## Bugs and other issues:
### Fixed Issues
Word prints down as a column. 
- FIX: add **end=" "** to print statement to make it a row.

When turning letters of the word to underscore, word_to_blank function returns 10 character instead of 6. Is it counting "" and []-characters? The extra symbols are coming from the API. 
Like this:
![](doc/readme-images/readme-glitch1.png "")
- FIX: added code to remove unwanted letters/symbols from the random word.

Creating a infinite loop when guessing a letter.

Adding same letter to the guessed letters list, only showing the first correctly guessed letter
- Fixed, order that code was read was wrong.

Printing error message 6 times (once for each letter). 
- fixed *for letter in word*

Showing the whole word when guessing a letter

Game doesnt loop, or keeps looping without letting user to give a new value

User can input more than one letter. 
- Fixed, but if user gives another invalid answer right after, the game closes.

If user gives an invalid answer more than once the game closes. 
- Fixed with while loop.

Trying to add the number of wrong answers and correct answers correctly. 
- Ended up having a global variable for these and guessed letters, as well as game_on, that triggers the ending.


### Not fixed

When replayed, game needs to fetch a new word, and clean up the list of the guessed letters.

When getting a random word, needs to pick a word from list. Currently only picking a random letter.

Replay currently not functional. Since time is running out, it will be saved for another day.



### Testing with code validators

Tested with **PEP8**. Found issues fixed.

### DEPLOYMENT
- Site was deployed to **Github Pages**.
- From Github, I chose the current project **Hangman-game** and **Settings**.
- On the leftside of the page there is **Pages**.
- Choose the **Main** branch
- Site will be published.
- This site is published at:


# CREDITS

## Mentor: 
Once again, thank you [Simen Daehlin](https://github.com/Eventyret/eventyret) for being my mentor!

## Random Word Library:
[Random Word API](https://random-word-api.herokuapp.com/home)

## Code:
[Remove character from string](https://www.journaldev.com/23674/python-remove-character-from-string)
```
 s = 'abc12321cba'

print(s.translate({ord(i): None for i in 'abc'}))

```

## Validator:

[PEP8](http://pep8online.com/)

## Other things I used while coding this game:

Balsamiq wireframes

[Text to ASCII generator](https://patorjk.com/software/taag)
