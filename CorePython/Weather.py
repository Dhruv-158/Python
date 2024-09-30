import requests
import json
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

city = input("Enter the name of the city = ")

url = f"https://api.weatherapi.com/v1/current.json?key=0135c83df7a9436185b162405243103&q={city}"

r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
print(wdic)
Weather_Temp = wdic["current"]["temp_c"]
cloud = wdic["current"]["cloud"]
print(f"The current weather Temprature in {city} is {Weather_Temp} degrees")
speak(f"The current weather Temprature in {city} is {Weather_Temp} degrees")
print(f"The current weather Cloud in {city} is {cloud} ")
speak(f"The current weather Cloud in {city} is {cloud} ")