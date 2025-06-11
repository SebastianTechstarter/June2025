# https://catfact.ninja/fact

import requests, datetime, time

for i in range(100):
    fact = requests.get("https://catfact.ninja/fact")
    print(fact)  ## printet die response in den terminal
    with open("catfacts.txt", "a") as file:
        file.write(
            f"{datetime.datetime.now()}: " + fact.json()["fact"] + "\n"
        )  ## fact.json() macht aus der Response ein dict
        time.sleep(5)  ## Computer pausiert 5 Sekunden
