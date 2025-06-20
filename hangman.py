import random

# Predefined word list
word_list = ['apple', 'brain', 'chair', 'dance', 'eagle']
word = random.choice(word_list)

# Game variables
guessed_letters = []
attempts = 6
display_word = ['_' for _ in word]

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print(f"You have {attempts} incorrect guesses allowed.")

# Game loop
while attempts > 0 and '_' in display_word:
    print("\nWord:", ' '.join(display_word))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single alphabetic character.")
        continue

    if guess in guessed_letters:
        print("🔁 You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                display_word[i] = guess
    else:
        attempts -= 1
        print(f"❌ Incorrect! Attempts left: {attempts}")

# Game result
if '_' not in display_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The word was:", word)
