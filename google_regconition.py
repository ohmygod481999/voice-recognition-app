import speech_recognition as sr

def recognizeAudio(name):
    r = sr.Recognizer()
    file = sr.AudioFile(name)
    with file as source:
        audio = r.record(source)
    try:
        text = r.recognize_google(audio, language = 'vi-VN', show_all = True )
        return text
        # print("I thinks you said '" + r.recognize_google(audio) + "'")
    except LookupError:                               
        print("Could not understand audio")