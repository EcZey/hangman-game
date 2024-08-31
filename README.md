# Hangman Game

Welcome to the Hangman Game project! This is a simple Python implementation of the classic Hangman game, where players guess letters to uncover a hidden word before running out of attempts.

## Project Overview

This project is a Python-based Hangman game that selects a random word from a predefined list. The player must guess the letters of the word, with each incorrect guess costing a life. The game continues until the player either successfully guesses the entire word or runs out of lives.

## Features

- **Random Word Selection**: The game randomly selects a word from a list of words.
- **Player Interaction**: Players can guess letters, and the game will provide feedback on whether the guess is correct or incorrect.
- **Visual Feedback**: The game displays the current progress of the word and the remaining lives.
- **Game Over Conditions**: The game ends when the player either correctly guesses the word or loses all their lives.

## Installation

To run the Hangman game on your local machine, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/EcZey/hangman-game.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd hangman-game
    ```
3. **Run the game**:
    ```bash
    python main.py
    ```


## How to Play

- When the game starts, a random word is selected, and you need to guess the letters one by one.
- If you guess a letter correctly, it will appear in the correct positions in the word.
- If you guess a letter incorrectly, you will lose a life.
- The game ends when you guess the word or lose all your lives.



