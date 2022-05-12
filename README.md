# Mine Hunter

Mine Hunter is a fun and interactive single player game which can be played in the Code Institute mock python terminal. This game is a mixture between traditional favourites Minesweeper and Battleship where the aim of the game is to locate and destroy all enemy mines before it is too late!!!

## The Game

<br>

![Image of game in mock terminal](assets/images/readme-intro.jpg)

<br>

This game is hosted by Heroku and can be played at:
<br>
[Mine Hunter](https://minehunter-sc.herokuapp.com/)

## **Contents**

## **How To Play**

*   Read the game instructions carefully
*   If player is happy to proceed press Y or Press N if more time is needed
*   Once started the player is now the Mine Hunter
*   The Mine Hunter is presented with a gameboard of 8 x 8 squares (64 squares total)
*   There are 10 mines hidden on the gameboard and the Mine Hunter must destroy all mines in order to win the game
*   Mine locations can be guessed by their co-ordinates (1-8 for the rows and A-H for the columns). All mines are placed randomly every time a new game is started.
*   The Mine Hunter has 25 turns in order to destroy all mines and win
*   Unselected squares are marked with an empty space
*   If a correct location is chosen the mine will be destroyed and will be replaced by an X. The Mine Hunter will also gain 2 extra turns.
*   If incorrect guess is made a - symbol will mark that location. 1 turn will be lost every time this happens.
*   If all 10 mines are destroyed before turns run out then the Mine Hunter will win the game otherwise it will be a loss.
*   At the end of the game an option will be presented to play again. Press Y to play again or press N to end that game session.


## **The Design Process**

### User Stories:

### Game Aims:

### How This Will Be Achieved:

### Game Flow Chart:

[Back To Contents](<#contents>)

## **Features**

### Existing Features:

####  Mine Hunter Welcome Screen:

This is the screen that the player will be presented with first when they access the terminal. It welcomes the player and gives them a number of very clear and concise instructions about how to play the game and what it will take to win. From here the player can decide if they wish to proceed with the game and they can do so by pressing Y.

<br>

![Image of Mine Hunter welcome screen](assets/images/readme-welcome.jpg)

#### The Gameboard:

The Mine Hunter will now be presented with a blank gameboard. They will be a able to view 64 empty square spaces. There are 10 mines placed randomly amongst these spaces. Rows are marked vertically via numbers 1-8 and columns are marked horizontally via letters A-H.

<br>

![Image of Mine Hunter blank gameboard](assets/images/readme-gameboard.jpg)

#### The Game Starts: 

Mine locations can be guessed via the above co-ordinates. The Mine Hunter is first asked to guess a row number 1-8 and secondly a column letter A-H. Numbers and letters outside of these ranges will not be accepted and will result in a message stating this. You also cannot guess the same square twice. After guessing they will notified via on screen text if they were successful and have a made a direct hit. They will be presented with one the following statements:

*   Well Done, that is a direct hit!!!
    You have gained 2 turns!!!

*   Sorry, that was not a direct hit!!!
    You have lost 1 turn!!!

A direct hit will result in a mine being destroyed and will be marked by an X. An unsuccesful attempt will br marked by an - symbol.

How many turns the Mine Hunter has remaining will always be displayed above the gameboard.

<br>

![Image of Mine Hunter gameplay](assets/images/readme-gameplay.jpg)

#### The Game Ends:

There are two possible outcomes of this game:

*   The Mine Hunter has guessed all 10 mine locations. The mines have been destroyed and they are victorious. If this happens the message below will be displayed:

Congratulations, you have destroyed all mines!!!')
You are the winner!!!

*   The Mine Hunter has not been successful with their guesses. All the mines have not be destroyed and all turns have run out resulting in defeat.

You Have 0 turns remaining
Sorry, you ran out of turns, the game is over.

* Regardless of the game outcome the Mine Hunter will be presented with an opportunity to restart the game via the Y or N option. Pressing Y will restart and return to the welcome screen and pressing N will end the game session.

<br>

![Image of Mine Hunter end game screen](assets/images/readme-endgame.jpg)

### Future Features:

*   Create an option for the Mine Hunter to create a username before the beginning of gameplay.

*   Include a timer to test how quickly the Mine Hunter can destroy all the mines.

*   Create a leaderboard to include the above usernames and score times. This would all allow for a much more enjoyable experience as the Mine Hunter would keep returning to play and beat their previous scores.

*   Create a multiplayer mode where 2 or more players can play at once on numerous game boards and the fastest to clear all mines would win.

*   Improve the games visuals. Add images and color to the gameboard/ text thus making the gameplay much more aesthetically pleasing.

*   Add audio and/ or sound effects for direct hits and misses.

<br>

[Back To Contents](<#contents>)

## **Data Model**

<br>

[Back To Contents](<#contents>)

## **Technologies Used**

*   [Python](https://html.spec.whatwg.org/) - Programming language used to build the game.
*   [Heroku](https://www.heroku.com/) - This was used to deploy the finished game.
*   [Github](https://github.com/) - This was used to store, track and manage the Git repository for the game.
*   [Gitpod](https://www.gitpod.io/) - Provided the development environment for the game.

<br>

[Back To Contents](<#contents>)

## **Testing**



