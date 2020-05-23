#Import imortant modules
import speech_recognition as sr
import pyperclip
import pyttsx3
import pyautogui as pya
import time

#for text to speech
engine = pyttsx3.init()
David = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'
engine.setProperty('rate', 130)
engine.setProperty('volume', 1.0)
engine.setProperty('voice', David)


#functon for copy the clipboard
def copy_clipboard():
    pya.hotkey('ctrl', 'c')
    time.sleep(.01)
    return pyperclip.paste()

def speak(audio):
    print("Jarvis: " + audio)
    engine.say(audio)
    engine.runAndWait()
#mic in infinite loop
while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('Next Command sir....')
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio)
            print('user: ', query)

            if "read" in query:
                pya.tripleClick(pya.position())
                zahid = []
                var = copy_clipboard()
                zahid.append(var)
                read = " ".join(zahid)
                print(read)
                speak(read)

        except:
            print("sorry sir! \n I didn\'t get that! \n Try typing the command" )
