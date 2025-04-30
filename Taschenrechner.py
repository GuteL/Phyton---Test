def main(): 
    global zahl1	
    global zahl2
    global rechenart
    global ergebnis
    zahl1 = input("Gib eine Zahl ein: ")	

    while True:
        rechenart = input("Gib die Rechenart ein: ")
        if rechenart in ["+", "-", "*", "/"]: 
            break  
        else:
            print("Die Rechenart ist nicht korrekt. Bitte versuche es erneut.")
            
    zahl2 = input("Gib eine zweite Zahl ein: ")
    print(f"{zahl1} {rechenart} {zahl2}")
    rechne()
    
    while True:
        weiter_rechnen = input("Willst du weiter rechnen, dann gib eine Rechenart ein, ansonsten etwas anderes: ")
        if weiter_rechnen in ["+", "-", "*", "/"]:
            rechenart = weiter_rechnen
            zahl1 = ergebnis
            zahl2 = input("Gib eine zweite Zahl ein: ")
            rechne()
        else:
            print("Das Programm wird beendet.")
            break
    
def rechne():
    global zahl1
    global zahl2
    global rechenart
    global ergebnis
    if rechenart == "+":   
        ergebnis = int(zahl1) + int(zahl2) 
        print(f"{zahl1} + {zahl2} = {ergebnis}")
    elif rechenart == "-": 
        ergebnis = int(zahl1) - int(zahl2) 
        print(f"{zahl1} - {zahl2} = {ergebnis}")
    elif rechenart == "*":
        ergebnis = int(zahl1) * int(zahl2)
        print(f"{zahl1} * {zahl2} = {ergebnis}")
    elif rechenart == "/":
        ergebnis = int(zahl1) / int(zahl2)
        if int(zahl2) == 0:  
            print("Durch 0 teilen ist nicht erlaubt")
        else:
            print(f"{zahl1} / {zahl2} = {ergebnis}")


main()
