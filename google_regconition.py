import speech_recognition as sr
r = sr.Recognizer()

file = sr.AudioFile('output.wav')
with file as source:
    audio = r.record(source)
    
print(audio)
try:
    text = r.recognize_google(audio, language="vi-VI", show_all = True )
    print(text)
    
except LookupError:                               
    print("Could not understand audio")