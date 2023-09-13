from win32com.client import Dispatch
speak = Dispatch("SAPI.SpVoice")

speak.Speak("write what you want to say")
while True:
    x=input("write what you want to say:")
    if x=="q":
        break
    speak.Speak(x)
speak.Speak("Bye Bye Friend have a nice day")