from API import api_key
import requests
api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=' + api_key + '&q='

# check input thrice
for x in range(3):
    city = raw_input("City name: ")
    # append
    url = api_address + city
    try:
        status = requests.get(url)
        status.raise_for_status()
        json_data = requests.get(url).json()

        result = "Today we're expecting... " + json_data['weather'][0]['main'] + ".\nSpecifically, " + \
                 json_data['weather'][0]['description'] + "."
        print result

    except requests.RequestException, e:
        print "Invalid City specified. \n Please retry with a valid City, " + str((x+2 - (2*x))) + " tries left.\n"

print "\nEnd of program, exiting."