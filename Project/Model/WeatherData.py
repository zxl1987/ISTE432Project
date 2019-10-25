from Data.apiData import *
from adapterData import *

class Getdata:
    datainfo = None
    weatherinfo=None

    def __init__(self, option, city):
        getWeather = apiData(option, city)
        adapter = Adapter(getWeather)
        self.datainfo = adapter
        self.processData()


    def processData(self):
        data=self.datainfo.alldata()
        if 'message' in data:
            if 'Invalid API key' in data['message']:
                self.weatherinfo= "Service Downtime. Please try again later."
            if 'city not found' in data['message']:
                self.weatherinfo = "Invalid input. Please re-enter."
            if '400' in data['cod']:
                self.weatherinfo="Geographic coordinates not found. Please re-enter."
        else:
            minTemp = (int(data['main']['temp_min']) - 273.15) * 9 / 5 + 32
            maxTemp = (int(data['main']['temp_max']) - 273.15) * 9 / 5 + 32
            Temp = (int(data['main']['temp']) - 273.15) * 9 / 5 + 32
            self.weatherinfo = [data['name'], round(minTemp, 2), round(maxTemp, 2), round(Temp, 2), data['wind']['speed'], data['weather'][0]['description']]

    def getWeatherInfo(self):
        return self.weatherinfo

