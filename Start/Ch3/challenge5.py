import json
import statistics

def countDays():
    with open("../../sample-weather-history.json", "r") as weatherfile:
        weatherdata = json.read(weatherfile)
    
    def averageTemp(d):
        return (d['tmin'] + d['tmax']) / 2

    winters = ["-12-","-01-","-02-"]
    winterMonths = [d for d in weatherdata if any([month in d['date'] for month in winters])]

    avgTemps = [averageTemp(d) for d in winterMonths]
    avgMean = statistics.mean(avgTemps)

    outlierTemp = avgMean + statistics.stdev(avgTemps) * 2
    outliers = [d for d in winterMonths if averageTemp(d) >= outlierTemp]

    return len(outliers)