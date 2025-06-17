import speech_recognition as sr

recognition = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something!")
    recognition.adjust_for_ambient_noise(source)  ## Lautstöre abgleichen
    audio = recognition.listen(source)


with open("voice_to_text.txt", "a") as file:
    file.write(recognition.recognize_google(audio, language="de-DE") + "\n")

print(
    "Du hast folgendes gesagt: " + recognition.recognize_google(audio, language="de-DE")
)
