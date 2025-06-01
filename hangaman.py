import random

HANGMAN = [
    '''
      +---+
          |
          |
          |
         ===''', '''
      +---+
      O   |
          |
          |
         ===''', '''
      +---+
      O   |
      |   |
          |
         ===''', '''
      +---+
      O   |
     /|   |
          |
         ===''', '''
      +---+
      O   |
     /|\\  |
          |
         ===''', '''
      +---+
      O   |
     /|\\  |
     /    |
         ===''', '''
      +---+
      O   |
     /|\\  |
     / \\  |
         ==='''
]

WORDS = ["python", "love", "coding", "hangman", "console", "github"]

def play_hangman():
    word = random.choice(WORDS)
    guessed = ['_'] * len(word)
    tries = 0
    guessed_letters = []

    print("🎯 Welcome to Hangman! 🎯")

    while tries < len(HANGMAN) - 1:
        print(HANGMAN[tries])
        print("Word: " + " ".join(guessed))
        print("Guessed letters: ", " ".join(guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessed[i] = guess
            if "_" not in guessed:
                print("You guessed it! The word was:", word)
                break
        else:
            tries += 1
            print("Wrong guess!")

    if tries == len(HANGMAN) - 1:
        print(HANGMAN[tries])
        print("Game over 💀 The word was:", word)

# Run the game
play_hangman()
