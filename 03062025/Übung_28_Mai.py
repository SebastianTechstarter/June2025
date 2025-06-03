# # Debugging vom 28. Mai

# Debug 1
zahl = 10
ergebnis = zahl + 5
print(ergebnis)
# Die Zahl war kein INT oder FLOAT, sondern ein String, mit dem nicht gerechnet werden kann.


# Debug 2
x = 3
if x > 0:
    print("x ist positiv")
# Einrückung fehlte, sodass der Printbefehl nicht als zum if gehörend erkannt wurde.

# Debug 3
for i in range(5):
    print(i)
# Doppelpunkt und Einrückung fehlten.


# Debug 4
alter = 18
if alter == 18:
    print("Volljährig")
# Bei dem Vergleich, ob die Variable alter = 18 ist fehlte das zweite "=", außerdem muss das print eingrückt werden.


# Debug 5
x = 4
y = 2
z = x ^ y
print("Ergebnis ist", z)
# Was passiert hier nochmal ? Was ist ^? Hinweis: Bitweise Operatoren
# Hier handelt es sich um den XOR-Operater und er verrechnet die Variablen x und y in binär miteinander.
# Das binäre Ergebnis wird als Dezimalzahl ausgegeben.


# Debug 6
x = 10
if x > 0:
    if x < 5:
        print("klein")
    else:
        print("groß")
# Die Einrückungen waren fehlerhaft bzw. fehlten ganz.


# Debug 7
while True:
    print("Hallo")
# Hinweis: Endlosschleife
# Da True immer wahr ist, wird die Schleife endlos das Wort "Hallo" ausgeben.
# Außerdem fehlt die Einrückung.

# Debug 8
eingabe = input("Gib eine Zahl ein: ")
if eingabe > 10:
    print("größer als 10")
# Einrückung fehlte, sodass klar ist, dass print zum if gehört.
# Es führt außerdem zum Abbrch des Programms, wenn die eingegebene Zahl kleiner oder gleich 10 ist.
