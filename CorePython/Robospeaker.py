
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

if __name__ == '__main__':
    print("welcome to RobotSpeaker 1.1 Created by me")
    speak("hello! how can i help you")
    while True:
        x = input("Enter What you Want me to speak : ")
        if  x =="stop" or x =="Stop":
            speak('bye bye')
            break
        Command = x
        speak(Command)


# For hindi 
# engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_HI-IN_HEMANT_11.0')

# For Gujarati
# engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_GU-IN_HEMANT_11.0')
