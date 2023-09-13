import requests
import json
city= input("enter city which you want to know: ")
url = f"http://api.weatherapi.com/v1/current.json?key=e5a3159d4be041508e4102034232703&q={city}"
r = requests.get(url)
#print(r.text)
wdic = json.loads(r.text)
print("temprature of {city} in celius")
print(wdic["current"]["temp_c"])
print("temprature of {city} in foranhite")
print(wdic["current"]["temp_f"])