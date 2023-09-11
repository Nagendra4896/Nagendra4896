import webbrowser
import time 
import pyttsx3

tts = pyttsx3.init('sapi5')

while True:
    time.sleep(120)
    tts.say("By the one and only Paardhu, behold the rick roll")
    tts.runAndWait()
    webbrowser.open_new_tab("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")
