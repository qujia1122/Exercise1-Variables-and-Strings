import random

def main():
    print("Welcome to Hangman!")
    words = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    secret_word = random.choice(words)
    attempts = 10
    guessed_letters = []
    guessed_word = ['_' for _ in secret_word]

    while attempts > 0 and '_' in guessed_word:
        print(f"Attempts left: {attempts}")
        print("Current word: ", ' '.join(guessed_word))

        letter = input("Guess a letter: ").lower()

        if not letter.isalpha():
            print("Invalid character. Please enter a single letter.")
            continue

        if letter in guessed_letters:
            print("You have already guessed that letter. Try again.")
        else:
            guessed_letters.append(letter)

        if letter in secret_word:
            print("Correct!")
            for i in range(len(secret_word)):
                if secret_word[i] == letter:
                    guessed_word[i] = letter
        else:
            print("Wrong guess. Try again.")
            attempts -= 1

    if '_' not in guessed_word:
        print("Awesome! You guessed the word correctly.")
        print(f"You guessed the word: {secret_word}")
    else:
        print("Thank you for playing. Better luck next time.")
        print(f"The word was: {secret_word}")

    print("Thank you for playing. See you next time.")


if __name__ == "__main__":
    main()