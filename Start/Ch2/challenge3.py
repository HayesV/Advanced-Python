import json
from functools import reduce

def miserableDay():
    with open("../../sample-weather-history.json", "r") as weatherfile:
        weatherdata = json.read(weatherfile)

    misery = reduce(dayRank,weatherdata)
    return misery

def miseryScore(d):
    wind = 0 if d['awnd'] is None else d['awnd']
    misery = (wind + (d['prcp']*10) + (d['tmax']*0.8)) / 3

    return misery

def dayRank(acc,elem):
    return acc if miseryScore(acc) >= miseryScore(elem) else elem