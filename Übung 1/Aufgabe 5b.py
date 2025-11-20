#grma1075 94731
class Aufgabe_5b:
    geheimes_wort = "halloHKA"

    while True: 
        passwort_eingabe = input("Bitte geben Sie das Passwort ein:")

        if passwort_eingabe == geheimes_wort:
            print("Zugriff gewährt!")
            break
        else:
            print("Falsch. Versuche es erneut.")
    