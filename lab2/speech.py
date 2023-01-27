# Reference: https://realpython.com/python-speech-recognition/#putting-it-all-together-a-guess-the-word-game

import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

print(r.recognize_google(audio))
