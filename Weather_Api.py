import requests



def format_response(weather_data):
    try:
        city_name = weather_data['name']
        condition = weather_data['weather'][0]['description']
        temperature = weather_data['main']['temp']
        icon_name = weather_data['weather'][0]['icon']
        weather_report = 'city :%s \ncondition: %s \ntemperature (°F): %s' %(city_name, condition, temperature)
    except:
        weather_report = "Oops!, Failed to retrieving information"
        icon_name =''
    return(weather_report, icon_name)         


def weather_information(city_name):
    weather_key ='7c2ee3f11d362db37c438743939ccaaa'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {"APPID":weather_key, "q" : city_name, "units" : "imperial"}
    response = requests.get(url, params)
    weather_data = response.json()
    weather_report = format_response(weather_data)
    return weather_report
print(weather_information('Dhaka'))    

    
