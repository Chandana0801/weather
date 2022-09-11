import requests
import ospython

from datetime import datetime

user_api = os.environ['current_weather_data']
location = input("Enter the city name: ")
#pasted from website: api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api

api_link = requests.get(complete_api_link)
api_date = api_link.json()
print(api_data)

if api_date['cod']=='404':
    print ("Invalid City:{}, Please check your city name".format(location)
else:
    #create variables to store and display data
    temp_city = ((api_daat['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']
    date_time = datetime.now().strftime("%d %b %y | %I:%M:%S %P")

    print ("----------------------------------------------")
    print ("Weather Stats for - {} || {}".format(location.upper(),date_time))
    print ("----------------------------------------------")

    print("current temperature is: {:.2f}deg c".format(temp_city))
    print("current weather desc :",weather_desc)
    print("current humidity :",hmdt,'%')
    print("current wind speed :",wind_spd,'kmph')