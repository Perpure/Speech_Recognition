import Levenshtein as Lev
import codecs
import speech_recognition as sr
N_TESTS = 5
r = sr.Recognizer()




def emulate_recognize(s):
    s = s.replace('.', '')
    s = s.replace(',', '')
    s = s.replace('!', '')
    s = s.replace('?', '')
    s = s.lower()
    return s


for i in range(1, 6):
    file = codecs.open('tests/Text' + str(i) + '.txt', 'r', 'cp1251')
    original_text = file.read()
    original_text = original_text.encode('cp1251').decode('utf8')
    original_text = emulate_recognize(original_text)
    raw = sr.AudioFile('tests/Test' + str(i) + '.wav')
    with raw as source:
        audio = r.record(source)
    recognized_text = r.recognize_google(audio, language='ru-RU')
    recognized_text = recognized_text.lower()
    file_out = open('tests/TextRecognized' + str(i) + '.txt', 'w')
    file_out.write(recognized_text)
    distance = Lev.distance(recognized_text, original_text)
    percentage = 100 - distance / max(len(recognized_text), len(original_text)) * 100
    print(percentage)
