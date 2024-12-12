Explanation of the Code:
Words List: A list of words from which a random word will be chosen.
choose_word(): This function selects a random word from the list.
display_word(): This function displays the word with guessed letters filled in and underscores for unguessed letters.
hangman(): The main game loop where the game logic occurs:
Tracks guesses, both correct and incorrect.
Allows the player to guess one letter at a time.
Ends the game either when the word is completely guessed or when the maximum number of incorrect guesses is reached.
Input validation: Ensures the user inputs a single letter and handles repeated guesses.
Game Over Conditions: If the player runs out of guesses, the game will display the correct word and end. If the player guesses all the letters correctly, they win.
Features:
Maximum 6 incorrect guesses are allowed.
The game displays the current state of the word with blanks and reveals correct letters.
The player gets feedback for each guess.
To play the game, just run the script in any Python environment. It will select a random word and ask the user for guesses.
