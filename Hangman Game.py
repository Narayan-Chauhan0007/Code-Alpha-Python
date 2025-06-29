import random

# Predefined word list
word_list = ["apple", "tiger", "plane", "chair", "grape"]

# Randomly select a word
secret_word = random.choice(word_list)
guessed_letters = []
attempts_left = 6

# Display word with underscores for unguessed letters
def get_display_word(word, guessed):
    return " ".join([letter if letter in guessed else "_" for letter in word])

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have", attempts_left, "incorrect guesses allowed.\n")

# Game loop
while attempts_left > 0:
    display_word = get_display_word(secret_word, guessed_letters)
    print("Word:", display_word)
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❗ Please enter a single valid alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!\n")
    else:
        attempts_left -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts_left}\n")

    if all(letter in guessed_letters for letter in secret_word):
        print("🎉 Congratulations! You guessed the word:", secret_word)
        break
else:
    print("😢 You've run out of guesses. The word was:", secret_word)

print("Thanks for playing Hangman!")
