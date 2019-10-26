import speech_recognition as sr
import json
import wave
from math import ceil

print("Working...")
file = open("Interview.txt", 'w')
file.close()
r = sr.Recognizer()
try:
    raw_wav = wave.open("Interview.wav", 'rb')
except FileNotFoundError:
    print("Put \"Interview.wav\" in this directory!")
    input()
else:
    fpm = raw_wav.getframerate() * 60
    n = ceil(raw_wav.getnframes() / fpm)
    for i in range(n):
        wav = wave.open("Audio_parts/Interview_temp{}.wav".format(i), 'wb')
        wav.setparams(raw_wav.getparams())
        wav.setnframes(fpm)
        wav.writeframes(raw_wav.readframes(fpm))
        wav.close()
        interview = sr.AudioFile("Audio_parts/Interview_temp{}.wav".format(i))
        with interview as source:
            audio = r.record(source)
        file = open("Interview.txt", 'w+')
        try:
            recognized_text = r.recognize_google(audio, language='ru-RU')
            file.write(recognized_text)
        except:
            print("Seems like this part of audio is corrupt or contains nothing")
        file.close()
        print("{}/{} done".format(i + 1, n))
        print(recognized_text)
    print("Success!")
    input()
