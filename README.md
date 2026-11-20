# Hangman Game

A command-line Hangman game built with Python as part of my Datheon internship.

The game selects a random word from a word list, and the player must guess the word one letter at a time before running out of attempts.

## Features

- Random word selection from an external word list.
- Interactive command-line gameplay.
- ASCII hangman drawings that update after incorrect guesses.
- Displays correctly guessed letters and hidden letters.
- Input validation to accept only single alphabetic characters.
- Prevents players from guessing the same letter twice.
- Limits incorrect guesses to six.
- Detects when the player wins or loses.

## Technologies Used

- Python 3
- `random` module
- Python sets
- File handling

## Project Structure

```text
datheon-internship-hangman/
│
├── hangman.py
├── google-10000-english-no-swears.txt
└── .gitignore
```

## Getting Started

### Prerequisites

- Python 3 installed on your computer.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/salamibenbolu-ui/datheon-internship-hangman.git
   ```

2. Navigate into the project folder:

   ```bash
   cd datheon-internship-hangman
   ```

3. Run the game:

   ```bash
   python hangman.py
   ```

**Important:** Keep `google-10000-english-no-swears.txt` in the same directory as `hangman.py`.

## How to Play

1. Run the Python file.
2. The game selects a secret word.
3. Enter one letter at a time.
4. Correct guesses reveal letters in the word.
5. Incorrect guesses add another part to the hangman drawing.
6. You have six incorrect guesses before the game ends.
7. Guess the complete word to win!

## What I Learned

While building this project, I practised:

- Python functions and parameters.
- Lists and list methods.
- Sets and duplicate detection.
- Conditional statements and loops.
- Reading data from external text files.
- Random selection.
- User input validation.
- Breaking a problem into smaller steps.

## Author

**Salami Benjamin**

GitHub: [@salamibenbolu-ui](https://github.com/salamibenbolu-ui)

## Project Context

This project was developed as part of my Datheon internship, where I practised Python programming and problem-solving.
