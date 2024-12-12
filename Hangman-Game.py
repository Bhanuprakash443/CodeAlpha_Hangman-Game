import random

# List of words for the game
words = ["python", "hangman", "programming", "developer", "keyboard", "challenge"]

def choose_word():
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman():
    word = choose_word()  # Select a random word
    guessed_letters = []  # To track guessed letters
    incorrect_guesses = 0  # To count incorrect guesses
    max_incorrect_guesses = 6  # Maximum incorrect guesses allowed

    print("Welcome to Hangman!")
    print(f"Try to guess the word. You have {max_incorrect_guesses} incorrect guesses allowed.")
    
    # Main game loop
    while incorrect_guesses < max_incorrect_guesses:
        print("\nCurrent word: " + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        # Validate the input
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only a single letter.")
            continue
        
        # Check if the letter was already guessed
        if guess in guessed_letters:
            print("You've already guessed that letter. Try a different one.")
            continue

        guessed_letters.append(guess)

        # Check if the guessed letter is in the word
        if guess in word:
            print(f"Good job! The letter '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Oops! The letter '{guess}' is not in the word.")
            print(f"You have {max_incorrect_guesses - incorrect_guesses} incorrect guesses left.")
        
        # Check if the player has won
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You've guessed the word: {word}")
            break

    # If the player runs out of guesses
    if incorrect_guesses == max_incorrect_guesses:
        print(f"\nSorry, you've lost. The word was: {word}")

# Run the game
if __name__ == "__main__":
    hangman()
