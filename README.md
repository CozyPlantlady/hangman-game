- [Hangman game](#hangman-game)
  * [Strategy](#strategy)
  * [Scope](#scope)
    + [User goals:](#user-goals-)
    + [User Stories:](#user-stories-)
  * [Structure of the game](#structure-of-the-game)
    + [Start:](#start-)
    + [The game:](#the-game-)
    + [The End / Game Over](#the-end---game-over)
  * [Skeleton:](#skeleton-)
  * [Surface:](#surface-)
  * [Testing with code validators](#testing-with-code-validators)
  * [User Testing](#user-testing)
    + [As a user I can start the game.](#as-a-user-i-can-start-the-game)
    + [As a user I feedback about how to play the game.](#as-a-user-i-feedback-about-how-to-play-the-game)
    + [As a user I can guess a letter.](#as-a-user-i-can-guess-a-letter)
    + [As a user I can choose to replay.](#as-a-user-i-can-choose-to-replay)
  * [Bugs and other issues:](#bugs-and-other-issues-)
    + [Fixed Issues](#fixed-issues)
    + [Not fixed](#not-fixed)
  * [DEPLOYMENT](#deployment)
    + [Before deploying](#before-deploying)
    + [GitHub](#github)
    + [Heroku](#heroku)
  * [CREDITS](#credits)
    + [Mentor:](#mentor-)
    + [Random Word Library:](#random-word-library-)
    + [Code:](#code-)
    + [Validator:](#validator-)
    + [Other things I used while coding this game:](#other-things-i-used-while-coding-this-game-)

# Hangman game
When I was in school, we used to play hangman on the classrooms chalkboard. It was exciting to try to guess, while the poor stick figure man was getting drawn... It's easy to learn, but hard enough to keep you entertained! So for my third project I'll make a hangman game you can play for your own fun.

## Strategy
**Hangman** is a classic word-guessing game, where user has to guess the right word. If user guesses wrong, the stick character gets another part drawn. When user has guessed wrong six times, it's game over. If user guesses all the letters right they win. 
This game is suitable for anyone who understands english language, but its very easily translated to other languages that use latin-script alphabet. By changing the wordlist or API the game can be fit to different themes. I have chosen to use random word API with random letter length, but this too is easily customisable. I decide against letting user choose the letter length or difficulty in this project, since I want the game to start right away. Too many options are not always good.

User will most likely wish to challenge themselves, and be entertained.

## Scope
Game lets the user guess untill they get the word right, or until they guess wrong six times. Game is unlimitedly replayable, as long as there is words left in the API (and there sure is).

### User goals:
What is their goal? What problem does this product or feature solve for them?
- It's a game, and user wants to be challenged and entertained.

### User Stories:
- As a user I can start the game.
- As a user I get feedback about how to play the game.
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

**Correct Answer**

![](doc/readme-images/readme-correct-answer.png "")

**Wrong Answer**

![](doc/readme-images/readme-wrong-guess.png "")

### The End / Game Over
When user guesses all the letters in the word, a winning picture is printed. User is asked if they want to play again.

**Picture from testing stage**

![](doc/readme-images/readme-win.png "")

If user looses, a different picture is printed. The word is revealed. User is asked if they want to play again.

** Game Over screen in final game**

![](doc/readme-images/readme-game-over.png "")

## Skeleton:
The main challenge of this project for me was making the game loop, user input loop, and how to get data from one function to another. 

After a lot of testing and failing, I chose to use **global variables** when I needed to get the variable updated several times during the game.

**User input** needs to be changed to *uppercase* and it can only be a single letter that is in alphabet. Currently user can still give åäö-letters, even though they wont be found in the words. Any invalid input gives an error message, and let's user to try again without them losing any points.

**Random Word API** gives a random english word. For this project it's chosen to give a random word of any length. While test playing it has given some really weird words, and it could be ideal to make a wordlist of more suitable words. However, using an API is part of what I wanted to learn in this project.

**The End or Replay?** I was planning to have a replay in this game. However, I was runnign out of time, and chose to draw the line there. You can find the almost ready replay functions pushed to the **GitHub**, and then removed from game. This would have not been a big loss for the player, since they can just **run the program again** after playing, which is as quick as clicking a "Y" to play again.

After my last mentor meeting I was encouraged to take afinal look about the replay function, and got valuable tips on how to do it. Hence, the replay option was added to the final version of the game!

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

## Testing with code validators

Tested with **PEP8**. Found issues fixed.

## User Testing

### As a user I can start the game.
As a user, I open the [app](https://game-that-is-like-hangman.herokuapp.com/). I see the text that tells me the rules of the game, and text *Let's start!* This tells me that the game has already started and is waiting for my input.

### As a user I feedback about how to play the game.
As a user, I'm given a quick reference of the rules when I start the game. When I guess a letter, I get feedback to know if my guess was wrong or right. I can see from the list of letters which letters I have already guessed. The hangman picture changes with every incorrect answer, which tells me how the game is going. 

### As a user I can guess a letter.
As a user, I can guess a letter. If I guess right, the game says "Correct! *letter* is in the word!" and prints the the word with correctly guessed letters showing.

If I guess wrong, game says "Sorry, *letter* is not in this word. Then game prints out the picture of the gallow and guessed letters.

If I give an invalid answer, like accidentally push a key twice, the game doesn't count it as a guess and I can guess again. 

### As a user I can choose to replay.
After I have finished the game (no matter if I lost or win) the game asks if I want to play again. It suggest for me to give Y or N as an answer, meaning yes or now. If I say Y, the game starts from beginning.
If I answer N, or anything else, the game ends and I see a message that thanks me for playing.

## Bugs and other issues:
### Fixed Issues
Word prints down as a column. 
- FIX: add **end=" "** to print statement to make it a row.

When turning letters of the word to underscore, word_to_blank function returns 10 character instead of 6. Is it counting "" and []-characters? The extra symbols are coming from the API. 
Like this: ["yoking"]
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

When game is run on Heroku, the hangman-logo is not visible unless scrolled up. This is because there is a lot of text printed at once. Can be fixed by adjusting what is printed first. 
- Fix: First hangman picture removed for now.

User can cheat the game by giving any right letter until game counts that the word is long enough.
- Fix: Moved the user_guess funtion to the game.py folder, so that it could access the global GUESSED_LETTERS variable. This makes sure that if a letter is in the word, but already guessed, it wasn't sent to guessed letters list as a duplicate.

When replayed, game needs to fetch a new word, and clean up the list of the guessed letters.
- Fixed with a new function for getting a new word, and status_quo function to set the game to starting point after user has chosen to play again.

When getting a random word, needs to pick a word from list. Currently only picking a random letter.
- Fixed. Not a list, but a new function (suggested by mentor), that fetches a new word.

### Not fixed

It's been reported that when played, the game doesn't always take the user input. Currently unsolved. Possibly issue with timing out.

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


## CREDITS

### Mentor: 
Once again, thank you [Simen Daehlin](https://github.com/Eventyret/eventyret) for being my mentor!

### Random Word Library:
[Random Word API](https://random-word-api.herokuapp.com/home)

### Code:
[Remove character from string](https://www.journaldev.com/23674/python-remove-character-from-string)
```
 s = 'abc12321cba'

print(s.translate({ord(i): None for i in 'abc'}))

```
[How to import modules from another folder](https://blog.finxter.com/python-how-to-import-modules-from-another-folder/)


### Validator:

[PEP8](http://pep8online.com/)

### Other things I used while coding this game:

Balsamiq wireframes

[Text to ASCII generator](https://patorjk.com/software/taag)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>
