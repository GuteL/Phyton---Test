def main(): 
    global zahl1	
    zahl1 = input("Gib eine Zahl ein: ")	
    global zahl2
    zahl2 = input("Gib eine zweite Zahl ein: ")
    global rechenart

    # Überprüfen, ob die Rechenart korrekt ist
    while True:
        rechenart = input("Gib die Rechenart ein: ")
        if rechenart in ["+", "-", "*", "/"]: 
            break  
        else:
            print("Die Rechenart ist nicht korrekt. Bitte versuche es erneut.")
    
    print(f"{zahl1} {rechenart} {zahl2}")
    rechne()
    
    
def rechne():
    global zahl1
    global zahl2
    global rechenart
    if rechenart == "+":    
        print(f"{zahl1} + {zahl2} = {int(zahl1) + int(zahl2)}")
    elif rechenart == "-":  
        print(f"{zahl1} - {zahl2} = {int(zahl1) - int(zahl2)}")
    elif rechenart == "*":
        print(f"{zahl1} * {zahl2} = {int(zahl1) * int(zahl2)}")
    elif rechenart == "/":
        if int(zahl2) == 0:  
            print("Durch 0 teilen ist nicht erlaubt")
        else:
            print(f"{zahl1} / {zahl2} = {int(zahl1) / int(zahl2)}")


main()