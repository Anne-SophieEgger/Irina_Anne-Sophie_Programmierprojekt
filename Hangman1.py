import random
word_list = ["apfel", "banane", "kirsche", "orange", "zitrone",
    "Blume", "Buch", "Tisch", "Stuhl", "Schule",
    "Baum", "Fenster", "Tür", "Sonne", "Mond",
    "Stern", "Wolke", "Regen", "Wind", "Feuer",
    "Wasser", "Erde", "Luft", "Vogel", "Fisch",
    "Affe", "Maus", "Kuh", "Pferd", "Elefant",
    "Löwe", "Tiger", "Giraffe", "Schaf", "Ziege",
    "Hase", "Frosch", "Biene", "Spinne", "Käfer",
    "Ei", "Milch", "Brot", "Kuchen", "Tee",
    "Kaffee", "Saft", "Wasser", "Wein", "Salz",
    "Zucker", "Butter", "Öl", "Nudeln", "Reis",
    "Kartoffel", "Tomate", "Gurke", "Zwiebel", "Knoblauch",
    "Paprika", "Apfel", "Banane", "Orange", "Erdbeere",
    "Zitrone", "Pfirsich", "Melone", "Ananas", "Traube",
    "Kiwi", "Birne", "Kirsche", "Brombeere", "Himbeere",
    "Blaubeere", "Avocado", "Möhre", "Spinat", "Brokkoli",
    "Erbse", "Salat", "Tomate", "Zucchini", "Aubergine",
    "Paprika", "Pilz", "Zitrone", "Orange", "Banane",
    "Pflaume", "Birne", "Aprikose", "Mango", "Kiwi",
    "Granatapfel", "Kaktusfeige", "Litschi", "Maracuja", "Guave"]


print(word_list)


def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Rate ein Buchstaben oder Wort: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Diesen Buchstaben hast du schon geraten.", guess)
            elif guess not in word:
                print(guess, "kommt nicht vor.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Bravo,", guess, "kommt im Wort vor!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("Das Wort hast du schon geraten", guess)
            elif guess != word:
                print(guess, "ist nicht das Wort.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Das geratene Wort ist zu kurz/lang.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Bravo, Du hast das richtige Wort erraten!")
    else:
        print("Sorry, du hast keine Versuche mehr. Das Wort war " + word)

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Neustart? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()

