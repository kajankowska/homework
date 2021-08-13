import sys
import datetime
import requests

# api_key = sys.argv[1]
# weatherdate = sys.argv[2]


def __init__(self, date, town):
    self.date = datetime.datetime.strptime(sys.argv[2], "%Y-%m-%d").date()


def api_data_downloading():
    url = "https://community-open-weather-map.p.rapidapi.com/forecast/daily"

    querystring = {"q": "Warszawa", "lat": "Warszawa", "lon": "Warszawa", "cnt": "16", "units": "metric or imperial"}

    headers = {
        'x-rapidapi-key': "7750c7f283mshe36073c5c257e9ap13cfd3jsnf1c5e55acf6e",
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    rowdata = response.json()
    newdata = {}

    for data in rowdata["list"]:
        dt = data["dt"]
        print(dt)
        weather = data["weather"][0]["main"]
        print(weather)
        newdata[dt] = weather
    return newdata


print(api_data_downloading())
