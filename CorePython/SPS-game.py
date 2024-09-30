import random
import pyttsx3
import time

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def play_with_device():
    print("You play with device")
    speak("You play with device")
    time.sleep(5)
    actions = ["stone", "paper", "scissor"]
    device_choice = random.choice(actions)
    player_choice = input("Enter your choice: ")

    if player_choice == device_choice:
        print("Match is a draw")
        speak("Match is a draw")
        
    elif (player_choice == "stone" and device_choice == "scissor") or \
         (player_choice == "scissor" and device_choice == "paper") or \
         (player_choice == "paper" and device_choice == "stone"):
        print(f"You win! \n device_choice is {device_choice}")
        speak(f"You win! \n device_choice is {device_choice}")
        
    else:
        print(f"You lose! \n device_choice is {device_choice} and your choice is {player_choice}")
        speak(f"You lose! \n device_choice is {device_choice} and your choice is {player_choice}")
        
      
def one_vs_one():
    print("you play 1 vs 1")
    speak("you play 1 vs 1")
    time.sleep(5)
    player1_choice = input("Enter player1 choice: ")
    player2_choice = input("Enter player2 choice: ")

    if player1_choice == player2_choice:
        print("Match is a draw")
        speak("Match is a draw")
    elif (player1_choice == "stone" and player2_choice == "scissor") or \
         (player1_choice == "scissor" and player2_choice == "paper") or \
         (player1_choice == "paper" and player2_choice == "stone"):
        print(f"player1 win! \n player2_choice is {player2_choice}")
        speak(f"player1 win! \n player2_choice is {player2_choice}")
    else:
        print(f"player1 lose! \n player2_choice is {player2_choice} and your choice is {player1_choice}") 
        speak(f"player1 lose! \n player2_choice is {player2_choice} and your choice is {player1_choice}")
        
print("welcome")
speak("welcome")
print("HOW you want to play (play with device) , (1 vs 1) ? please enter you choice")
speak("HOW you want to play (play with device) , (1 vs 1) please enter you choice")

speak("if you want to play with computer Enter 1 and you want to play 1 vs 1 Enter 2 = ")
user_choice =input("if you want to play with computer Enter 1 and you want to play 1 vs 1 Enter 2 = ")
if user_choice == "1":
    print("user_choice is 1")
    speak("user_choice is 1 that mean user want to play with device")
    play_with_device()
elif user_choice == "2":
    print("user_choice is 2")
    speak("user_choice is 2 that mean user want to play one vs one")
    one_vs_one()
else:
    print("Invalid choice, please select the correct option.") 
    speak("Invalid choice, please select the correct option.")   
    
