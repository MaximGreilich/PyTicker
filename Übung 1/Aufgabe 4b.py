#grma1075 94731
class Aufgabe_4b:
    print("Geben Sie Ihre Note ein")
    note = input()
    note_float = float(note)

    if note_float < 4.0 and note_float > 1.0:
        print("Prüfung bestanden!")
    elif note_float > 4.0 and note_float <= 5.0:
        print("Prüfung leider nicht bestanden.")
    else:
        print("Ungültige Note.")
    