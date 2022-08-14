
import requests

API_KEY = "PERSONAL API"
city = input('whats the city that you want to get weather forcast? ')
print (city)


print ( 'Displaying weather report for' + city)

url = 'https://wttr.in/{}'.format(city)

res = requests.get(url)

try:
  print(res.text)
except:
  print("the city not found")
