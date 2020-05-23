import speech_recognition as sr
import pyperclip
import time
import pyautogui as pya

while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print('Next Command sir....')
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio)
            print('user: ', query)

            if 'copy' in query:
                pya.tripleClick(pya.position())
                pya.hotkey('ctrl', 'c')
                time.sleep(.01)
                copied = pyperclip.paste()
                print('copy bhai')


            elif "pet" in query:
                copy_list = []
                copied = pyperclip.paste()
                copy_list.append(copied)
                copied_item = " ".join(copy_list)
                pyperclip.paste()
                print(pyperclip.paste())
        except:
            print("Next Command" )
