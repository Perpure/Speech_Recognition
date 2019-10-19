import speech_recognition as sr
import json

print("Working...")
r = sr.Recognizer()
try:
    interview = sr.AudioFile("Interview.wav")
    with interview as source:
        audio = r.record(source)
except FileNotFoundError:
    print("Put \"Interview.wav\" in this directory!")
    input()
else:
    file = open("Interview.txt", 'w')
    try:
        file.write(r.recognize_google(audio, language='ru-RU'))
        file.close()
    except json.decoder.JSONDecodeError:
        print("Your request is empty or the Internet connection lost")
        input()
    except sr.RequestError:
        print("Request error. Probably your file is too large")
        input()
    else:
        print("Success!")
        input()
