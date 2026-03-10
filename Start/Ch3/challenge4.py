import json
import random

def select_days(year, month):
    with open("../../sample-weather-history.json", "r") as weatherfile:
        weatherdata = json.read(weatherfile)

    #concactenate date into year month
    yearmonth = year + "-" + month

    def ymFilter(day):
        if yearmonth in day['date']:
            return True
        return False
    
    ymData = list(filter(ymFilter,weatherdata))
    ymList = random.sample(ymData, k=5)

    return ymList


