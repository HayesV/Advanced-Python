# Example file for Advanced Python: Hands On by Joe Marini
# Introspect the data to make some determinations

import json
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# TODO: What was the warmest day in the data set?
#lambda function called over and over again on each element in the data
warmDay = max(weatherdata, key=lambda x: x['tmax'])
print(f"The warmest day was {warmDay['date']} at {warmDay['tmax']} degrees")


# TODO: What was the coldest day in the data set?

coldDay = min(weatherdata, key=lambda x: x['tmin'])
print(f"The coldest day was {coldDay['date']} at {coldDay['tmin']} degrees")

# TODO: How many days had snowfall?
#list comprehension creates a new list in concise syntax

snowDays = [day for day in weatherdata if day['snow'] > 0 ]
print(f"Snow fell on {len(snowDays)} days")
pprint.pp(snowDays)