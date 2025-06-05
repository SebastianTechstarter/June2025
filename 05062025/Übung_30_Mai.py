# Debug 1 :
a = [1, 2, 3]
b = a.copy()
b[0] = 99
print("a =", a)
print("b =", b)
# Frage: Warum wird a[0] ebenfalls zu 99, obwohl wir nur b verändert haben?
# selbe Schublade mit zwei Etiketten. Es ist zweimal dieselbe Liste, die angesprochen wird.
# Wie kann man das verhindern?
# Liste a kopieren, sodass die ursprüngliche Liste a unverändert bleibt.

# Debug 2 :
farben = ["rot", "gruen", "blau"]
print(farben[0])
# Frage: Was passiert hier? Was wäre die korrekte Lösung?
# Die die Stelle 3 wird abgerufen, diese existiert aber nicht. korrekt wäre entweder die Stelle zu löschen oder eine Stelle 0, 1 oder 2 zu wählen.

# Debug 3:
zahlen = [1, 2, 3, 4]
doppelt = [x + x for x in zahlen if x % 2]
print(doppelt)
# Frage: Warum sind nur bestimmte Zahlen im Ergebnis?
# Was macht die Bedingung if x % 2 genau?
# Die Bedingung prüft, ob die Zahl ungerade ist. Nur ungerade Zahlen werden ausgewählt und verdoppelt, sodass "2(1 aus der Liste)" und "6(3 aus der Liste)" ausgegeben werden.

# Debug 4:
tupel = (1, 2, 3)
tupel[1] = 5
print(tupel)
# Frage: Warum funktioniert das nicht?
# Tupel sind unveränderlich und somit kann der Wert nicht überschrieben werden.

# Debug 5:
daten = ("Ali", [10, 20])
daten[1].append(30)
print(daten)
# Frage: Wie kann sich der Inhalt hier verändern, obwohl Tupel eigentlich unveränderlich sind?
# der Inhalt wird am Ende erweitert, also "30" wird angehängt. Die urpsrüngliche Liste wird ja nicht verändert, sondern nur erweitert.

# Debug 6:
farben = {"rot": "#FF0000", "gruen": "#00FF00", "blau": "#0000FF"}
for schluessel, wert in farben.items():
    print(f"{schluessel} = {wert}")
# Frage: Warum wird hier nur der Schlüssel ausgegeben?
# Wie müsste man den Code ändern, um rot = #FF0000 usw. zu sehen?
