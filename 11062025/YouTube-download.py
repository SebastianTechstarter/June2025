from pytubefix import YouTube

url = input("Was möchtest Du downloaden? (Bitte Link eingeben) ")
# YouTube(url).streams.get_highest_resolution().download()
# YouTube(url).streams.get_audio_only().download()

youtube_format = input("Welches Format möchtest Du haben? (audio / video) ")

if youtube_format == "video":
    print("Video wird heruntergeladen...")
    YouTube(url).streams.get_highest_resolution().download("/Users/sebas/Downloads")
    print("Video wurde erfolgreich heruntergeladen.")

elif youtube_format == "audio":
    print("Audio wird heruntergeladen...")
    YouTube(url).streams.get_audio_only().download("/Users/sebas/Downloads")
    print("Audio wurde erfolgreich heruntergeladen.")

else:
    print("erlaubte Eingaben sind nur 'audio' oder 'video' ")
