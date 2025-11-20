#grma1075 94731
class Aufgabe_4a:
    print("Geben Sie Ihr Alter ein")
    alter = input()
    alter_int =int(alter)
    if alter_int <= 12: 
        print("Der Eintritt kostet 5€")
    elif alter_int <=17 and alter_int >= 12:
        print("Der Eintritt kostet 8€")
    elif alter_int >=65:
        print("Der Eintritt kostet 7€ (Seniorentarif)")
    else:
        print("Der Eintritt kostet 12€(Normaltarif)")
