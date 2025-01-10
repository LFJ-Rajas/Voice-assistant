import speech_recognition as sr
from googletrans import Translator

# 1) Listen : Hindi or English
def Listen():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source,0,8)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="hi")

    except:
        return ""

    query=str(query).lower()
    return query


#2) Translate

def Translation(Text):
    line = str(Text)
    translate= Translator()
    result=translate.translate(line)
    data=result.text
    return data

def mic():
    query=Listen()
    data=Translation(query)
    return data

def for_waking_up():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source,0,8)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en")

    except:
        return ""

    query=str(query).lower()
    return query