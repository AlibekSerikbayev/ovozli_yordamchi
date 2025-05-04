import speech_recognition as sr

def recognize_uzbek():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Gapiring...")
        audio = r.listen(source)
    try:
        return r.recognize_google(audio, language="uz-UZ")
    except:
        return "Ovoz tanilmadi"
