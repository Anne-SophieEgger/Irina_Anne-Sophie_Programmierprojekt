import random

# Liste von Wörtern für das Spiel
words = ["python", "hangman", "computer", "programming", "algorithm"]

# Zufälliges Wort auswählen
word = random.choice(words)

# Anzahl der Versuche des Spielers
tries = 6

# Buchstaben, die der Spieler bereits geraten hat
guessed_letters = []

# Schleife für das Spiel
while tries > 0:
    # Anzahl der noch nicht geratenen Buchstaben
    remaining_letters = [letter if letter in guessed_letters else '_' for letter in word]
    
    # Ausgabe des aktuellen Spielstands
    print(' '.join(remaining_letters))
    print(f"Versuche übrig: {tries}")
    
    # Eingabe eines Buchstabens durch den Spieler
    guess = input("Rate einen Buchstaben: ").lower()
    
    # Überprüfung, ob der Buchstabe bereits geraten wurde
    if guess in guessed_letters:
        print("Du hast diesen Buchstaben bereits geraten. Bitte versuche es erneut.")
        continue
    
    # Hinzufügen des geratenen Buchstabens zur Liste der geratenen Buchstaben
    guessed_letters.append(guess)
    
    # Überprüfung, ob der Buchstabe im Wort enthalten ist
    if guess in word:
        print("Richtig geraten!")
        
        # Überprüfung, ob das Spiel gewonnen wurde
        if all([letter in guessed_letters for letter in word]):
            print("Glückwunsch, du hast gewonnen!")
            break
    else:
        print("Falsch geraten.")
        tries -= 1
        
        # Überprüfung, ob das Spiel verloren wurde
        if tries == 0:
            print(f"Das Wort war '{word}'. Du hast verloren.")
            break