# Debug 1
liste1 = [4, 5, 6]
liste2 = liste1.copy()
liste2.append(7)
print("Liste1:", liste1)
print("Liste2:", liste2)
# Frage: Warum enthält auch liste1 das Element 7? Wie kann man liste2 unabhängig kopieren?
# Beides mal dieselbe Liste. mit der Methode copy kann man Abhilfe schaffen.

# Debug 2
werte = [2, 4, 6, 8]
ergebnis = [x / 2 for x in werte if x < 5]
print(ergebnis)
# Frage: Welche Werte kommen in die neue Liste? Was bewirkt die Bedingung if x < 5?
# 1 und 2. Die Bedingung bewirkt, dass nur Zahlen genutzt werden, die kleiner 5 sind.

# Debug 3
farben = ["rot", "grün", "blau"]
farben_neu = farben
farben = ["gelb", "lila"]
print(farben_neu)
# Frage: Was wird ausgegeben? Warum ist farben_neu hier nicht betroffen?
# farben wird neu definiert und überschrieben. Kopieren ist hier nicht notwendig.

# Debug 4
person = ("Max", 28, "Berlin")
person[2] = "Hamburg"
# Frage: Warum funktioniert das nicht? Was müsste man tun, um einen ähnlichen Effekt zu erzielen?
# Es handelt sich hierbei um ein Tupel, das nicht überschrieben werden kann.

# Debug 5
daten = ("Ali", [100, 200])
daten[1][0] = 300
print(daten)
# Frage: Warum ist hier trotz eines Tupels eine Veränderung möglich?
# Innerhalb des unveränderlichen Tupels ist eine Liste, die veränderet werden kann.

# Debug 6
info = {"stadt": "Köln", "einwohner": 1000000}
print(info["fläche"])
# Frage: Warum gibt es hier einen Fehler? Wie kann man den Zugriff sicherer machen?
# "Fläche" gibt es nicht.


# Debug 7
def schreibe(text):
    return text.upper()


nachricht = schreibe("hallo")
print(nachricht)
# Frage: Warum ist die Ausgabe None? Wie müsste die Funktion geändert werden?
# das return ist leer und gibt nichts zurück.


# Debug 8
def addiere(x, y):
    return x + y


summe = addiere(3, 4)
print(summe)
# Frage: Warum kann man mit summe später nicht weiterrechnen?
# es fehlt der return. Ohne diesen wird "None" zurückgegeben und dies ist eine verrechenbare Zahl.

# Debug 9
x = "global"


def test():
    x = "lokal"


test()
print(x)
# Frage: Warum bleibt x nach dem Funktionsaufruf „global“?
# Es bleibt global, weil es vorher explizit als global definiert wurde.


# Debug 10
def info(stadt, name="Gast"):
    print(name, "aus", stadt)


info("Ali", "Berlin")

# Frage: Warum funktioniert diese Definition nicht? Wie muss die Reihenfolge der Parameter angepasst werden?
# Parameter mit einem Default-Wert müssen immer ans Ende der Liste gestellt werden.
