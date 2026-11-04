
import random

# Load words from the given word list
with open("google-10000-english-no-swears.txt", "r") as file:
    words = file.readlines()

# Clean the word list
words = [word.strip().lower() for word in words]
words = [word for word in words if word.isalpha()]

# Select a random secret word
secret_word = random.choice(words)

# Initialize game variables
guessed_letters = set()
mistakes = 0
max_mistakes = 6

# Different stages of the hangman drawing
stages = [
    """
     +---+
     |   |
         |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
         |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
    ========
    """,
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
    ========
    """
]


# Display the current hangman drawing
def display_gallows(mistakes):
    print(stages[mistakes])


# Display the hidden word
def display_word(secret_word, guessed_letters):
    for letter in secret_word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()


# Display game introduction
print("=" * 35)
print("       WELCOME TO HANGMAN")
print("=" * 35)

# Main game loop
while mistakes < max_mistakes:

    display_gallows(mistakes)

    print("\nWord: ", end="")
    display_word(secret_word, guessed_letters)

    print(f"\nIncorrect guesses: {mistakes}/{max_mistakes}")
    print(f"Guessed letters: {sorted(guessed_letters)}")

    # Get player's guess
    guess = input("\nEnter a letter: ").strip().lower()

    # Validate user input
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input! Enter only one letter.")
        continue

    # Check for duplicate guesses
    if guess in guessed_letters:
        print("You have already guessed that letter!")
        continue

    # Store the guessed letter
    guessed_letters.add(guess)

    # Check whether the guess is correct
    if guess in secret_word:
        print("Correct guess!")
    else:
        mistakes += 1
        print("Wrong guess!")

    # Check whether the player has won
    if all(letter in guessed_letters for letter in secret_word):
        print("\n" + "=" * 35)
        print("       CONGRATULATIONS!")
        print("          YOU WON!")
        print("=" * 35)
        print(f"The secret word was: {secret_word}")
        break

# Check whether the player has lost
if mistakes == max_mistakes:
    display_gallows(mistakes)

    print("\n" + "=" * 35)
    print("         GAME OVER!")
    print("=" * 35)
    print(f"The secret word was: {secret_word}")
    print("Better luck next time!")