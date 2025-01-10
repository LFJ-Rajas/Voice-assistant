import keyboard
import pyautogui
import webbrowser

from time import sleep

def opening(query):

    if "visit" in query:
        nameofweb = query.replace("visit ","")
        
        link= f"www.{nameofweb}.com"
        webbrowser.open(link)

    elif "open" in query :
        nameofapp=query.replace("open ","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(nameofapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)

    return True