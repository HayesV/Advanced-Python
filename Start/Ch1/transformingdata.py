# Example file for Advanced Python: Hands On by Joe Marini
# Transform data from one format to another

import json
import copy
import pprint

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# the map() function is used to transform data from one form to another
# TODO: Let's convert the weather data from imperial to metric units
def ToC(f):
    f = 0 if f is None else f
    return (f - 32) * 5/9


def ToMM(i):
    i = 0 if i is None else i
    return i * 25.4


def ToKPH(s):
    s = 0 if s is None else s
    return s * 1.60934


def ToMetric(wd):
    newWD = copy.copy(wd)
    newWD['tmin'] = ToC(wd['tmin'])
    newWD['tmax'] = ToC(wd['tmax'])
    newWD['prcp'] = ToMM(wd['prcp'])
    newWD['snow'] = ToMM(wd['snow'])
    newWD['snwd'] = ToMM(wd['snwd'])
    newWD['awnd'] = ToKPH(wd['awnd'])

    return newWD

# TODO: Use map() to call ToMetric and convert weatherdata to metric
metric_weather = list(map(ToMetric, weatherdata))
pprint.pp(weatherdata[0])
pprint.pp(metric_weather[0])


# TODO: use the map() function to convert objects to tuples
# in this case, create tuples with a date and the average of tmin and tmax
Avg_Temp = lambda t1, t2: (t1 + t2) / 2.0

tuple_data = list(map(lambda d:(d['date'], Avg_Temp(d['tmax'],d['tmin'])), weatherdata))
pprint.pp(tuple_data[0:5])