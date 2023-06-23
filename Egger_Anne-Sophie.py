
import random

def hangman():
    word_list = ["python", "hangman", "game", "openai", "programming"]
    word = random.choice(word_list).lower()
    guessed_letters = []
    tries = 6

    while True:
        print_hangman(tries)
        print_word(word, guessed_letters)

        if all(letter in guessed_letters for letter in word):
            print("Glückwunsch! Du hast das Wort erraten.")
            break

        if tries == 0:
            print("Du hast keine Versuche mehr. Das Wort war '{}'.".format(word))
            break

        guess = input("Errate einen Buchstaben: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Ungültige Eingabe. Bitte gib einen einzelnen Buchstaben ein.")
            continue

        if guess in guessed_letters:
            print("Du hast diesen Buchstaben bereits geraten.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            tries -= 1
            print("Leider falsch.")

def print_word(word, guessed_letters):
    for letter in word:
        if letter in guessed_letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()

def print_hangman(tries):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
        """,
        """
           --------
           |      |
           |      O
           |
           |
           |
        """,
        """
           --------
           |      |
           |
           |
           |
           |
        """
    ]

    print(stages[tries])

hangman()