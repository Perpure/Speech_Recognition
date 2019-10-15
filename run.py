import speech_recognition as sr
r = sr.Recognizer()
interview = sr.AudioFile("Interview.wav")
with interview as source:
    audio = r.record(source)
print(r.recognize_google(audio, language='ru-RU'))