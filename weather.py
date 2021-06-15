import requests

api_address = "http://api.openweathermap.org/data/2.5/weather?appid=0dd33d6ed066c80920162b0d3749e1e5&q="

def weather(city, state, url):
    # Gets weather from website, checks the connection status, and displays weather data for user
    r = requests.get("https://openweathermap.org")
    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print('Something went wrong: ', e)
        main()
    else:
        print('Your connection was successful! \n')
    json_data = requests.get(url).json()
    #print(json_data)                           # JSON formatted data that should not be printed for user
    country = json_data['sys']['country']
    temp = json_data['main']['temp']
    feels = json_data['main']['feels_like']
    minTemp = json_data['main']['temp_min']
    maxTemp = json_data['main']['temp_max']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    symbol = '\xb0' + 'F'                       # degrees Fahrenheit
    print('---------------------------------------')
    print("Current Weather Conditions for {}, {}, {}".format(city, state, country))
    print("Current Temperature: " + str(temp) + symbol)
    print("Feels Like Temperature: " + str(feels) + symbol)
    print("Today's High Temp: " + str(maxTemp) + symbol)
    print("Today's Low Temp: " + str(minTemp) + symbol)
    print("Humidity: " + str(humidity) + "%")
    print("Wind Speed: " + str(wind) + "mph")
    print('---------------------------------------')


def main():
    print("Welcome to the Weather App!\n \n")
    # Set initial value for user city
    city = ' '
    while city != "Q":
        city = input("Please enter a city name or \'q\' to quit. \n").upper()
        # state = input("Please enter the state or \'q\' to quit. \n").upper()
        if city == "Q":
            # End user's experience with app
            print("\n\nThanks for using my app. Come back to check the weather soon!")
            break
        else:
            # Construct the URL and call weather function
            state = input("Please enter the full state name. \n").upper()
            url = api_address + city + "," + state + "&units=imperial"
            weather(city, state, url)


main()
