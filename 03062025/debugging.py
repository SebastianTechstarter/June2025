# Debug 1


def begrüßung(name):
    print("Hallo " + name)


begrüßung("Seb")
# Frage: Warum funktioniert dieser Funktionsaufruf nicht?
# 1) Zwischen String "Hallo" und der Variablen name fehlte das "+"
# 2) die Funktion wurde ohne Argument aufgerufen. In die Klammern gehört ein Name in Anführungszeichen.


# Debug 2
def addiere(x, z, y=0):
    return x + y + z


# Frage: Warum akzeptiert Python diese Funktionsdefinition nicht?
# Die Parameter sind falsch angeordnet. Parameter mit Standardwert (y=0) muss nach hinten.
# Korrekt ist: def addiere(x, z, y=0)

# Debug 3
x = "global"


def test():
    global x
    x = "lokal"


test()
print(x)
# Frage: Warum bleibt x beim Wert “global”? Wie könnte man x innerhalb der Funktion global verändern?
# Die lokale Variante von x wird nur innerhalb der Funktion erstellt und hat keine globalen Auswirkungen, daher wird die globale Variante aufgerufen.
# Wenn nun das "global x" in die Funktion aufgenommen wird, so gilt x="lokal" global.


# Debug 4
def rechne(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Fehler, weil Division durch 0"


print(rechne(5, 0))
# Frage: Warum wird nichts zurückgegeben? Wie könnte man das verbessern?
# Die Funktion gibt im except-Fall nichts zurück, weil hierfür kein Return definiert ist.


# Debug 5
def teile(x, y):
    if y == 0:
        raise ZeroDivisionError("Division durch 0 ist nicht möglich.")
    return x / y


try:
    teile(4, 0)
except Exception as e:
    print("Fehler:", e)


# Frage: Ist die Fehlerbehandlung hier sinnvoll? Was fehlt in der Fehlermeldung?
# Der Code funktioniert, aber die Fehlermeldung ist leer. Deshalb habe ich eine Nachricht zum ZeroDivisionError hinzugefügt.


# Debug 6
def mache_etwas():
    try:
        x = int("abc")
    finally:
        print("Fertig")


mache_etwas()
# Frage: Was passiert hier und warum wird kein Fehler angezeigt?
# Die Funktion "mache_etwas()" soll versuchen, den Inhalt von x in ein Integer umzuwandeln. Da dies bei Buchstaben (abc) nicht möglich ist, passiert hier nichts weiter.
# Schlussendlich (Finally) wird "Fertig" ausgegeben.


# Debug 7
def berechne():
    try:
        return 10 / 0
    except ZeroDivisionError:
        print("Fehler")
    finally:
        return "Fertig"


print(berechne())
# Frage: Warum wird “Fertig” ausgegeben und nicht “Fehler”? Was ist der Einfluss von finally?
# Der Fehler wird durch das Except aufgefangen und "Fehler" gedruckt. Am Ende wird, egal wie die Division ausgeht, der finally-Befehl ausgeführt.
# finally überschreibt alle vorangegangen returns und gibt "Fertig" zurück.


# Debug 8
def konvertiere(zahl):
    try:
        return int(zahl)
    except ValueError:
        print("Ungültige Eingabe")


x = konvertiere("abc")
print(x + 1)

# Frage: Warum gibt es einen neuen Fehler, obwohl der erste abgefangen wurde?
# x ist der falsche Datentyp. Es wird eine Zahl verlangt, x ist aber, trotz abgefangenem Fehler, ein String
