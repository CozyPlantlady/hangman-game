# Hangman game
When I was in school, we used to play hangman on the classrooms chalkboard. It was exciting to try to guess, while the poor stick figure man was getting drawn... It's easy to learn, but hard enough to keep you entertained! So for my third project I'll make a hangman game you can play for your own fun.

## Strategy
**Hangman** is a classic word-guessing game, where user has to guess the right word. If user guesses wrong, the stick character gets another part drawn. When user has guessed wrong six times, it's game over. If user guesses all the letters right they win. 
This game is suitable for anyone who understands english language, but its very easily translated to other languages that use latin-script alphabet. By changing the wordlist or API the game can be fit to different themes. I have chosen to use random word API with random letter length, but this too is easily customisable. I decide against letting user choose the letter length or difficulty in this project, since I want the game to start right away. Too many options are not always good.

User will most likely wish to challenge themselves, and be entertained.

## Scope
Game lets the user guess untill they get the word right, or until they guess wrong six times. Game would be unlimitedly replayable, as long as there is words left.

### User goals:
What is their goal? What problem does this product or feature solve for them?
- It's a game, and user wants to be challenged and entertained.

### User Stories:
- As a user I can start the game.
- As a user I can find more information about how to play the game.
- As a user I can guess a letter.
- As a user I can choose to replay.

## Structure of the game
Original plan for the game

![](doc/readme-images/readme-wireframe.png "")

Final wireframe of the game
![](doc/readme-images/readme-wireframe-update.png "")

### Start:
When game is started, it first greets the user with logo and rules. User can start playing directly.
![](doc/readme-images/readme-welcome.png "")

*Rules was removed as it's own section, since the game is simple and rules can be viewed, if needed, at the start. This relieves user from making unnecessary choices*

### The game:
The main game loop lets user to input a letter. If the letter is in the word, it is shown in the  letter field in correct spot as well as added to the used letters list. 
If letter is incorrect, it's added to the used letters list, and user loses a point.
Game continues until all the letters in a word are guessed and word is revealed, or until user guesses wrong six times.

Correct Answer

![](doc/readme-images/readme-correct-answer.png "")

Wrong Answer

![](doc/readme-images/readme-wrong-guess.png "")

### The End / Game Over
When user guesses all the letters in the word, a winning picture is printed. Game ends.

![](doc/readme-images/readme-win.png "")

If user looses, a different picture is printed. The word is revealed.

![](doc/readme-images/readme-game-over.png "")

## Skeleton:
The main challenge of this project for me was making the game loop, user input loop, and how to get data from one function to another. 

After a lot of testing and failing, I chose to use **global variables** when I needed to get the variable updated several times during the game.

**User input** needs to be changed to *uppercase* and it can only be a single letter that is in alphabet. Currently user can still give åäö-letters, even though they wont be found in the words. Any invalid input gives an error message, and let's user to try again without them losing any points.

**Random Word API** gives a random english word. For this project it's chosen to give a random word of any length. While test playing it has given some really weird words, and it could be ideal to make a wordlist of more suitable words. However, using an API is part of what I wanted to learn in this project.

**The End or Replay?** I was planning to have a replay in this game. However, I was runnign out of time, and chose to draw the line there. You can find the almost ready replay functions pushed to the **GitHub**, and then removed from game. This is not a big loss for the player, since they can just **run the program again** after playing, which is quicker than choosing to replay after game has ended.

## Surface:
For the visual side of this project I decided to add ASCII art for both the logo and the hangman pictures. 

Logo was made with [Text to ASCII generator](https://patorjk.com/software/taag).

Hangman pictures were made by creator.
```
||======
||//   |
||/    |
||     o/ -Hey! I'm OK!
||    /|
||    / \
||
||.......
```


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
```
["yoking"]
```
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



## Testing with code validators

Tested with **PEP8**. Found issues fixed.

## DEPLOYMENT

### Before deploying
This project uses **request import**, so I added that to **requirements.txt**. This tells Heroku that **request** is needed for the code to run as intented. 
```
requests == 2.27.1
```
- You should be able to use **pip** to add required imports to the **requirements** automatically, but I had to find the needed code online and add it manually.

For the Heroku to be able to read **user input** I added *\n* to the end of the input field. 

### GitHub
For the deployment to Heroku to work, it's important to have the final version of the project pushed to GitHub. 
- *git add .* *git commit* and *git push* to make sure you have the latest changes in Github.

### Heroku
After logging in to **Heroku** choose *New*-button on the top right side of the screen, and choose *New app*

Choose the name off the app. Since it has to be unique, I chose *game-that-is-like-hangman*.

Choose your region 
- Mine is *Europe*.

Next to the **Settings**. You can find it from the *navigation bar*. Locate *Buildpacks*, and choose Python and NodeJs, in that order.

Still in *Settings*, locate *Config Vars*. 
- As suggested by Code Institute, I added *Config Var* with **key** of *PORT*, **value** of *8000*.

Changes are saved automatically.

Time to **Deploy**! Choose *Deploy* from *navigation bar*.

This projects chosen **Deployment method** is by being **Connected to GitHub**. 

After you are connected, give the name you used for your project in **GitHub**
- This project is *hangman-game* in **GitHub**.

I prefer deploying manually, so I chose **Manual deploy** and *main-branch*, *deploy branch*.

Game is published at: [Hangman game](https://game-that-is-like-hangman.herokuapp.com/)


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
