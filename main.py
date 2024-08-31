import random
from hangman_words import word_list
from hangman_art import logo, stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

print(logo)

# Create blanks
display = ["_" for _ in range(word_length)]

end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # Check if the user has already guessed the letter
    if guess in display:
        print(f"You've already guessed {guess}")
        continue  # Skip the rest of the loop if letter was already guessed

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # Check if user is wrong
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was {chosen_word}.")
            break

    # Display current progress
    print(f"{' '.join(display)}")

    # Check if user has got all letters
    if "_" not in display:
        end_of_game = True
        print("You win!")

    # Display the current stage of the hangman
    print(stages[lives])



