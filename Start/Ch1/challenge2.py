import json

with open("../../sample-weather-history.json","r") as weatherfile:
    weatherdata = json.read(weatherfile)

def get_day_temp_description():
    def tempData(t):
        averageT = (t['tmin'] + t['tmax']) / 2
        if averageT <= 60:
            return "cold"
        elif averageT >= 80:
            return "hot"
        return "warm"
    
    tupledData = list(map(lambda d:(d['date'], tempData(d)), weatherdata))
    return tupledData