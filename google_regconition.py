import speech_recognition as sr
r = sr.Recognizer()

file = sr.AudioFile('blob.wav')
with file as source:
    audio = r.record(source)
    
print(audio)
try:
    text = r.recognize_google(audio, language = 'en-IN', show_all = True )
    print("I thinks you said '" + r.recognize_google(audio) + "'")
except LookupError:                               
    print("Could not understand audio")