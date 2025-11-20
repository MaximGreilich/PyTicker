#grma1075 94731    
class Aufgabe_7b:
    def greet(name="Gast", is_first_time=False):
 
        if is_first_time:
            print(f"Willkommen, {name}!")
        else:
            print(f"Schön, dass du wieder da bist, {name}!")

    greet("Maxim", False)
    greet(name="Maxim", is_first_time=False)
    greet(is_first_time=False, name="Maxim")
    greet()

#Bei dem Aufruf mit den Keywordargumenten ist die Reihenfolge der Argumente egal, bei dem Aufruf mit Positionsargumenten
#muss die Reihenfolge genau so sein, wie bei der Definition der Funktion