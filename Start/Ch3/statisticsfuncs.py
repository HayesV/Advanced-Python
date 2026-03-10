# Example file for Advanced Python: Hands On by Joe Marini
# Using the statistics package

import json
import statistics

# open the sample weather data file and use the json module to load and parse it
with open("../../sample-weather-history.json", "r") as weatherfile:
    weatherdata = json.load(weatherfile)

# select the days from the summer months from all the years
summers = ["-06-","-07-","-08-"]
summer_months = [d for d in weatherdata if any([month in d['date'] for month in summers])]
print(f"Data for {len(summer_months)} summer days")

# TODO: calculate the mean for both min and max temperatures
maxTemps = [d['tmax'] for d in summer_months]
minTemps = [d['tmin'] for d in summer_months]

print(max_mean := round(statistics.mean(maxTemps),4))
print(min_mean := round(statistics.mean(minTemps),4))


# TODO: calculate the median values for min and max temperatures
print(round(statistics.median(maxTemps),4))
print(round(statistics.median(minTemps),4))

# TODO: use the standard deviation function to find outlier temperatures
upperOutlier = max_mean + (statistics.stdev(maxTemps) * 2)
lowerOutlier = min_mean - (statistics.stdev(minTemps) * 2)

print(round(upperOutlier,4))
print(round(lowerOutlier,4))

max_outliers = [t for t in maxTemps if t >= upperOutlier]
min_outliers = [t for t in minTemps if t <= lowerOutlier]

print(max_outliers)
print(min_outliers)