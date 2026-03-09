import json
import pprint

with open("../../sample-weather-history.json","r") as weatherfile:
    weatherdata = json.load(weatherfile)

def getCWR():

    def isCWR(d):
        tAvg = (d['tmax'] + d['tmin']) / 2
        totalPrcp = d['snow'] + d['prcp']
        if tAvg < 45 and totalPrcp > 0.7 and d['awnd'] > 10.0:
            return True
        return False
    
    badDays = list(filter(isCWR, weatherdata))

    return badDays
