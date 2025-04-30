with open("text.txt", "r") as datei:
    content = datei.read()
    print(content)


start_marker = "///"
end_marker = "///"
start_index = content.find(start_marker)
end_index = content.find(end_marker)


text = input("Geben Sie den Text ein, der zwischen den Markierungen eingefügt werden soll: ")   
neuer_inhalt = (
    content[:start_index + len(start_marker)] +
    text +
    content[end_index + len(end_marker):]
)


with open("text.txt", "w") as datei:
    datei.write(neuer_inhalt)