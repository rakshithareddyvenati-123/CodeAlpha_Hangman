import random

# List of predefined words
words = ["python", "computer", "hangman", "program", "student"]

# Select a random word
word = random.choice(words)

# Variables
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

print("================================")
print("      WELCOME TO HANGMAN")
print("================================")
print("Guess the word one letter at a time.")
print(f"You have {max_guesses} incorrect guesses.\n")

# Game loop
while incorrect_guesses < max_guesses:

    # Display the current progress
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if the word is completely guessed
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("✅ Correct guess!")
    else:
        incorrect_guesses += 1
        remaining = max_guesses - incorrect_guesses
        print("❌ Wrong guess!")
        print("Remaining incorrect guesses:", remaining)

# If player loses
if incorrect_guesses == max_guesses:
    print("\n💀 Game Over!")
    print("The correct word was:", word)