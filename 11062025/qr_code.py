import qrcode

link = input("Bitte hier Link einfügen: ")
img = qrcode.make(link)

name_of_image = input("Wie soll das PNG heißen? (.png wird automatisch angefügt): ")
img.save(f"{name_of_image}.png")
