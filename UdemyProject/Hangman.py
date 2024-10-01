import random

# List of words to choose from
word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the list
chosen_word = random.choice(word_list)
print(f"Pssst, the chosen word is: {chosen_word}")  # Debugging hint

# Create a placeholder for the word (initially all underscores)
word_length = len(chosen_word)
display = "_" * word_length
print(display)

# Flag to check if the game is over
game_over = False
correct_letters = []

# Loop until the game is over
while not game_over:
    guess = input("Guess a letter: ").lower()

    # Create an empty string to update the display for the current round
    updated_display = ""

    # Loop through each letter in the chosen word
    for letter in chosen_word:
        if letter == guess:
            updated_display += letter
            correct_letters.append(guess)  # Add correct guess to list
        elif letter in correct_letters:
            updated_display += letter  # Keep previously guessed letters
        else:
            updated_display += "_"

    display = updated_display  # Update the display
    print(display)

    # Check if the user has guessed all the letters
    if "_" not in display:
        game_over = True
        print("You Win!")
