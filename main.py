n = int(input("Welche Fakultät berechnen?"))
i = n
vorrechnung = i - 1
ergebnis = vorrechnung * n
i -= 1
fertig = False
while not fertig:
    vorrechnung = i - 1
    ergebnis = vorrechnung * ergebnis
    if i - 1 == 1:
        fertig = True
    else:
        i -= 1
print(ergebnis)
print("\r\n (" + str(len(str(ergebnis))) + " Stellen)")
