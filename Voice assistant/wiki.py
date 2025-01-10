import wikipedia
from Speaking import speak
def wiki(query):
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia","")
    results = wikipedia.summary(query) 
    speak("According to Wikipedia")
    print(results)
    speak(results)