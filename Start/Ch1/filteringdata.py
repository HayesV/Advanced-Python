# Example file for Advanced Python: Hands On by Joe Marini
# Filter values out of a data set based on some criteria

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# the filter() function gives us a way to remove unwanted data points
# TODO: create a subset of the data for days that had snowfall
snowDays = list(filter(lambda d:d['snow'] > 0.0, weatherdata))
print(len(weatherdata))
print(len(snowDays))


# TODO: pretty-print the resulting data set
pprint.pp(snowDays)

# filter can also be used on non-numerical data, like strings
# TODO: create a subset that contains summer days with heavy rain (more than 1 in, about 2.5cm)
def is_summer_rain_day(d):
    summerMonths = ["-07-","-08-"]
    if any([m in d['date'] for m in summerMonths]) and d['prcp'] >= 1.0:
        return True
    return False

summerRain = list(filter(is_summer_rain_day,weatherdata))

print(len(summerRain))
pprint.pp(summerRain)
