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
