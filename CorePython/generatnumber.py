import random
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

Computer_choice = random.randint(1,10)

while True:
    User_choice = int(input("Enter your guess Number "))
    
    if User_choice == Computer_choice:
        print(f"{User_choice} is a correct Guess") 
        speak("You won")
        break
    else:
        print(f"{User_choice} is wrong Guess")
        speak(f"you lose cause right Guess+ is {Computer_choice} ")    
