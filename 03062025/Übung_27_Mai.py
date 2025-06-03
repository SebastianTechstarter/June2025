# Debug vom 27 Mai
# Aufgabe 1:
zahl = 7
print(zahl)
# ungültige Syntax, aktuell ist das keine For-Schleife, sondern die Definition einer Variablen.
# Dies funktioniert aber so nicht, da "for" im Program bereits vorab fest definiert ist.

# Aufgabe 2:
name = "Ada"
if name == "Ada":
    print("Hello,", name)
# Fehlende Einrückung von "print" nach dem if-Statement

# Aufgabe 3:
price = 19.99  # Zahl
quantity = 3
total = price * quantity
print("Total:", total)
# Der Preis von 19.99 ist nur als String hinterlegt und keine Zahl, die verrechnet werden kann.
# Somit wird die Variable "total" keinen Gesamtpreis ausgeben, sondern den String dreimal hintereinander printen.
