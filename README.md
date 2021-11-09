# HANGMAN 1.1
## Playing Hangman

Hangman is an old school favorite, a word game where the goal is simply to find the missing word or words while given a hint.

Our version of this is the multiplayer, between two people, with Player 1 acting as the hint and solution giver, and Player 2 guessing the word with the hint given, letter by letter.

### CHANGELOG (07/11/2021):
1. Phrases can now be used in multiplayer
2. NEW MODE: singleplayer has finally been added with a plethora of new words




## Instructions to Run: 

To begin game:

1. Type python hangman.py in the shell.
2. Ensure Colorama and Art are installed or the code will not run.
3. type s for single player and m for multiplayer when prompted.

### Rules: 
###

#### MULTIPLAYER:
1. With Player two away from the screen, player one thinks of a word.
2. Player one then gives the computer a hint to the word, followed by the word itself before pressing enter.
3. Player two has to guess this word ONE LETTER AT A TIME.
4. If Player 2's chosen letter exists in the answer, then all asterisks in the answer where that letter appear will be revealed.
5. After you've revealed several letters, you may be able to guess what the answer is and fill in the remaining letters.
6. Be warned, every time Player 2 guesses a letter wrong, you loose a life and the hangman begins to appear, piece by piece. Player two gets six chances where each incorrect letter increases this count.

After guessing the word correctly, Player 2 WINS and if they have used all their chances they LOSE.
###
#### SINGLEPLAYER
1. Select your hint from the list of hints provided.
2. The computer will display the hint you select as well as asterisks showing the amount of letters in the word you need to guess.
3. Try to guess the word one letter at at time, each incorrect answer will result in the hangman being drawn.

After guessing the word correctly, You WIN and if you have used all your chances you LOSE.