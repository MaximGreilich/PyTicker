#grma1075 94731
class Aufgabe_3bc:
    print("Wählen Sie zwei zahlen")
    zahl1_str = input()
    zahl2_str = input()

    zahl1_str_float = float(zahl1_str)
    zahl2_str_float = float(zahl2_str)
    ergebnis = zahl1_str_float + zahl2_str_float
 
    print(ergebnis)
#Das Ergebnis wird wenn man die float-funktion nicht verwendet,
#hier einfach konkatiniert, da die einzelnen Zahlen als String gelesen werden