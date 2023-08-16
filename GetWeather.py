# TODO: save previous data and retrieve if user wants
from math import floor
import requests
import geocoder

# config is a file that holds my api key. it is hidden in the git ignore file
import config

with open("celsius_or_fahrenheit.txt", "r") as file:
    cOrF = file.read()
    if cOrF == "True":
        isF = True
    elif cOrF == "False":
        isF = False
    else:
        isF = None

API_KEY = config.api_key
isF = False
hasSavedData = False
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
g = geocoder.ip('me')
city = g.city
state = g.state

if cOrF == "":
    F = input("Would you like to use Celsius or Fahrenheit? ")
    if F[0].lower() == "c":
        isF = False
    else:
        isF = True

match isF:
    case False:
        request_url = f"{BASE_URL}?appid={API_KEY}&q={city},{state}&units=metric"
    case True:
        request_url = f"{BASE_URL}?appid={API_KEY}&q={city},{state}"

response = requests.get(request_url)
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    if not isF:
        temperature = data["main"]["temp"]
    elif isF:
        temperature = round(1.8*(data["main"]["temp"]-273) + 32, 2)

    tempStr = str(floor(temperature))

    print("\nWeather:", weather + "\n")

    if isF:
        print("Temperature:", temperature, "fahrenheit \n")
    else:
        print("Temperature:", temperature, "celsius \n")

    clre = input("Do you want a clothing recommendation? (y/n): ")

    temperature = round(1.8 * (data["main"]["temp"] - 273) + 32, 2)

    if clre == "y" or clre == "yes":
        if int(temperature) >= 90:
            print("You should probably wear short sleeves and shorts")
        if 90 > int(temperature) > 50:
            print("You should probably wear short sleeves and long pants.")
        if 50 >= int(temperature) > 37:
            print("You should probably wear a jacket and long pants.")
        if int(temperature) <= 37:
            print("You should probably wear a coat/jacket and long pants.")

    with open("celsius_or_fahrenheit.txt", "w") as file:
        file.write("")
        file.write(str(isF))
else:
    print("An error occurred.")
