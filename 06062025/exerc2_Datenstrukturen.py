# 1. Lies vom Benutzer eine Zeile mit Ganzzahlen, durch Leerzeichen getrennt, ein(Beispiel 3 3 1 4 3 2 1).
# 2. Speichere die Zahlen in einer Liste.

# 3. Erstelle anschließend
# eine Menge (set) mit allen einzigartigen Zahlen und
# ein Dictionary, das jeder Zahl ihre Häufigkeit zuordnet.

# 4. Gib aus
# die Gesamtzahl der eingegebenen Werte,
# die Menge der eindeutigen Zahlen,
# die Häufigkeit jeder Zahl, sortiert aufsteigend nach der Zahl.

users_list = input(
    "Gib mir eine Folge mit ganzen Zahlen, getrennt durch Leerzeichen: "
).split()
new_list = list(map(int, users_list))
# print(new_list)
new_set = set(new_list)
print(new_set)

count_dict = {}

for number in new_list:
    if number in count_dict:
        count_dict[number] += 1
    else:
        count_dict[number] = 1

print("Häufigkeiten: " + count_dict)
