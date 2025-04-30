with open("text.txt", "r") as datei:
    content = datei.read()
    print("Aktueller Inhalt der Datei:")
    print(content)

start_marker = "///"
end_marker = "///"


start_index = content.find(start_marker)
end_index = content.find(end_marker, start_index + len(start_marker))

if start_index == -1 or end_index == -1:
    print("Fehler: Markierungen nicht korrekt im Text gefunden.")
else:
    text = input("Geben Sie den Text ein, der zwischen den Markierungen eingefügt werden soll: ")
    
    
    neuer_inhalt = (
        content[:start_index + len(start_marker)] +  
        text +                                      
        content[end_index:]                        
    )

    
    with open("text.txt", "w") as datei:
        datei.write(neuer_inhalt)
    print("Der Text wurde erfolgreich aktualisiert.")