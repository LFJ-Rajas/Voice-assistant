from aibrain import Reply
from Listen import for_waking_up
from Listen import mic
from Speaking import speak
from opening import opening
import datetime
from wiki import wiki

import pyjokes
import webbrowser

import requests

if __name__=='main_':
    def mainexec():
        

        while True:
            data = mic()
            data = str(data)
            o_data=data
            li=data.split()
            print(f'You : {data}')

            if "visit" in data or "open" in data and len(li)==2:
                opening(" ".join(li))

            elif "time" in data or "current time" in data:
                strtime=datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir! The time is {strtime}")
                
            elif "wikipedia" in data:
                wiki(data)
            
            elif 'joke' in data:
                speak(pyjokes.get_joke())

            elif 'news' in data:
                news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
                speak('Here are some headlines from the Times of India,Happy reading')
                

            elif "write a note" in data:
                speak("What should i write, sir")
                note = mic()
                file = open('jarvis.txt', 'w')
                speak("Sir, Should i include date and time")
                snfm = mic()
            
            elif "show note" in data:
                speak("Showing Notes")
                file = open("jarvis.txt", "r")
                print(file.read())
                speak(file.read(6))
            
            elif "where is" in data:
                data = data.replace("where is", "")
                location = data
                speak("User asked to Locate")
                speak(location)
                webbrowser.open("https://www.google.nl/maps/place/" + location + "")
            
            elif "weather" in data:
                api_key=""
                base_url="https://api.openweathermap.org/data/2.5/weather?"
                speak("whats the city name")
                city_name=mic()
                complete_url=base_url+"appid="+api_key+"&q="+city_name
                response = requests.get(complete_url)
                x=response.json()
                if x["cod"]!="404":
                    y=x["main"]
                    current_temperature = y["temp"]
                    tempt= int(current_temperature)-273.15
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    speak(" Temperature in Celcius is " +
                        str(int(tempt)) +
                        "\n humidity in percentage is " +
                        str(current_humidiy) +
                        "\n description  " +
                        str(weather_description))
                    print(" Temperature in Celcius is = " +
                        str(int(tempt)) +
                        "\n humidity (in percentage) = " +
                        str(current_humidiy) +
                        "\n description = " +
                        str(weather_description))

                else:
                    speak(" City Not Found ")

            else:
                reply=Reply(o_data)
                print(f'Jarvis : {reply}')
                speak(reply)
                if "good bye jarvis" in o_data or "good bye javed" in o_data:
                    exit()
        
    def wakingup():
        query = for_waking_up()

        if "wake up" in query:
            print("WOKE UP")
            mainexec()
        else:
            wakingup()

    wakingup()