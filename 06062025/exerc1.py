# Aufgabe:
# Schreibe ein sehr kleines Konsolenprogramm, das genau eine Multiple-Choice-Frage stellt:
# Welche dieser Variablennamen ist in Python nicht erlaubt?
# A) my_var B) _var C) 2var D) var_2

# Das Programm soll:
# die Frage samt Antwortmöglichkeiten ausgeben,
# eine Eingabe A–D (Groß-/Kleinschreibung egal) entgegennehmen und
# zurückmelden, ob die Antwort richtig ist.
# Bei einer falschen Antwort soll zusätzlich erklärt werden,
# warum C korrekt wäre (Variablennamen dürfen nicht mit einer Ziffer beginnen).

print(
    "Welche dieser Variablennamen ist in Python nicht erlaubt?\n A) my_var B) _var C) 2var D) var_2"
)

answer = input().lower()
if answer == "c":
    print("Richtig, denn Variablen dürfen in Python nicht mit einer Zahl beginnen!")
else:
    print(
        "Leider Falsch. Die richtige Antwort ist C, da Variablen in Python nicht mit einer Zahl beginnen dürfen."
    )
