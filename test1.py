
import json
import pyowm


def getWind(lat, lon, api_key):
  owm = pyowm.OWM(api_key)
  weather = (owm.weather_at_coords(lat,lon)).get_weather()
  wind = weather.get_wind()
  return wind


text = open("./key.json", "r")
json_dict = json.load(text)
# json_dict['owm_key']


lon = 135.504954;
lat = 34.6525455;
wind = getWind(lat, lon, json_dict['owm_key'])
if 'def' in wind.keys():print(wind['deg'])
print(wind['speed']);

  
