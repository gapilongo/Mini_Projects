import random

# Game title
game_title = "Word Raider"

# Set up the list of words to choose from
word_bank = []
with open("words.txt") as word_file:
    for line in word_file:
        word_bank.append(line.rstrip().lower())  # Strip any trailing whitespace and convert to lowercase

# Pick a random word from the list
word_to_guess = random.choice(word_bank)

# Set up the game variables
misplaced_guesses = []  # List to track letters that are in the word but in the wrong position
incorrect_guesses = []  # List to track letters that are not in the word at all
max_turns = 5           # Maximum number of turns the player gets
turns_taken = 0         # Counter for the number of turns taken

# Display the initial game state
print("Welcome to", game_title)
print("The word has", len(word_to_guess), "letters.")
print("You have", max_turns - turns_taken, "turns left.")

# Main game loop
while turns_taken < max_turns:
    # Get the player's guess
    guess = input("Guess a word: ").lower()

    # Check if the guess length matches the word length and if it's all alphabetic
    if len(guess) != len(word_to_guess) or not guess.isalpha():
        print("Please enter a word with", len(word_to_guess), "letters.")
        continue

    # Process the player's guess
    index = 0  # To track the current position in the word
    for c in guess:
        if c == word_to_guess[index]:  # Correct letter in the correct position
            print(c, end=" ")
            if c in misplaced_guesses:  # Remove from misplaced if it's now correct
                misplaced_guesses.remove(c)
        elif c in word_to_guess:  # Correct letter but in the wrong position
            if c not in misplaced_guesses:
                misplaced_guesses.append(c)
            print("_", end=" ")
        else:  # Incorrect letter
            if c not in incorrect_guesses:
                incorrect_guesses.append(c)
            print("_", end=" ")
        index += 1

    # Move to the next line after printing the current guess
    print("\n")
    print("Misplaced letters: ", misplaced_guesses)
    print("Incorrect letters: ", incorrect_guesses)
    
    # Increment the turn counter
    turns_taken += 1

    # Check if the player has guessed the word correctly
    if guess == word_to_guess:
        print("Congratulations, you win!")
        break

    # Check if the player has used up all their turns
    if turns_taken == max_turns:
        print("Sorry, you lost. The word was", word_to_guess)
        break

    # Display the number of turns left and prompt for another guess
    print("You have", max_turns - turns_taken, "turns left.")
