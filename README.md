## Hangman (game)
The game Hangman application, final project for Intro to Computer Science.

## Authors
Sasha Mothershead, Minh Pham, and Zoe Pharo

## How to run
Ensure all necessary files in the same folder (Hangman.py, grade3.txt, grade4.txt, grade5.txt, and grade6.txt)
In the command line, type:
    python3 hangman.py

## Game Rules
    [Home screen opens]
    * Select grade level or click button for further instructions 
        * if you selected "instructions," click the "return to home screen" box to return to the home screen and start the game
    
    [Game screen opens]

    * The object of the game is to guess a randomly generated hidden word. The number of dashes on the screen corresponds to the number of letters in the hidden word. A "WIN" occurs if you guess the word in five attempts or less. A "LOSS" occurs if you guess incorrectly six or more times, and the hangman is fully drawn. 
    
    * Guess a letter by clicking a key on your keyboard
        * if the letter is correct, the letter appears on the corresponding line to represent its place in the word

        * if the letter is incorrect, a body part is added to the hangman and the incorrect letter will appear in the "wrong letters" box

        * if you guess a letter twice, nothing will happen and you will be prompted to guess again 
        
    * keep guessing by clicking additional keys on your keyboard until:
        * you win (the entire word is completed)
        OR 
        * you lose (entire hangman is complete)
        
    [end screen opens]
    
    * Choose whether you want to play again or not by clicking one of the buttons  
        * if you click "yes" the game will return to the homescreen and run again 
        * if you click "no" the window will close
