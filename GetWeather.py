from math import floor
import requests
import geocoder

# config is a file that holds my api key. it is hidden in the git ignore file
import config


API_KEY = config.api_key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
g = geocoder.ip('me')
city = g.city
state = g.state
request_url = f"{BASE_URL}?appid={API_KEY}&q={city},{state}"
response = requests.get(request_url)
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(1.8*(data["main"]["temp"]-273) + 32, 2)

    tempStr = str(floor(temperature))

    print("\nWeather:", weather + "\n")

    print("Temperature:", temperature, "fahrenheit \n")

    clre = input("Do you want a clothing recommendation? (y/n): ")

    if clre == "y" or clre == "yes":
        if int(temperature) >= 90:
            print("You should probably wear short sleeves and shorts")
        if 90 > int(temperature) > 50:
            print("You should probably wear short sleeves and long pants.")
        if 50 >= int(temperature) > 37:
            print("You should probably wear a jacket and long pants.")
        if int(temperature) <= 37:
            print("You should probably wear a coat/jacket and long pants.")

else:
    print("An error occurred.")
