# file = open("nassima.txt", "r")    # r -> read
# print(file.read())
# file.close()

# with open("nassima.txt", "r") as file:
#     print(file.read())

# with open("nassima.txt", "w") as file:
#     file.write("Ich liebe programmieren\n")

# with open("nassima.txt", "a+") as file:
#     file.write("Ich bin eine neu geschrieben Zeile\n")
#     print(file.read())


# datetime.datetime.now()
import datetime

timestamp = datetime.datetime.now()
with open("log.txt", "a") as logfile:
    logfile.write(f"{timestamp}: Ich bin eine neu geschrieben Zeile\n")


import meinMathModule as mmm


print(mmm.addieren(5, 8))
print(mmm.subtrahieren(5, 8))
