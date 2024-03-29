import sys
import os
cwd = os.getcwd()
parent_dir = (os.path.abspath(os.path.join(cwd, os.pardir)))
sys.path.append(parent_dir)

from Data.apiData import *
from adapterData import *
from Model.UserData import *
from Data.userInfo import *
user=UserData
userInfo=userInfo()

class WeatherData:
    dataInfo = None
    weatherInfo = None

    def __init__(self, option, city):
        getWeather = APIData(option, city)
        adapter = AdapterData(getWeather)
        self.dataInfo = adapter
        self.processData(option,city)


    def processData(self,option,city):
        data = self.dataInfo.allData()
        if 'message' in data:
            if 'Invalid API key' in data['message']:
                self.weatherInfo = "Service Downtime. Please try again later."
            if 'city not found' in data['message']:
                self.weatherInfo = "city not found. Please re-enter."
            if '400' in data['cod']:
                self.weatherInfo = "Geographic coordinates not found. Please re-enter."
        else:
	    if userInfo.getUserid():{
	  	  user.saveHistory(self,option,city)
	    }
            minTemp = (int(data['main']['temp_min']) - 273.15) * 9 / 5 + 32
            maxTemp = (int(data['main']['temp_max']) - 273.15) * 9 / 5 + 32
            temp = (int(data['main']['temp']) - 273.15) * 9 / 5 + 32
            humidity=int(data['main']['humidity'])
            self.weatherInfo = [data['name'], round(minTemp, 2), round(maxTemp, 2), round(temp, 2), data['wind']['speed'], data['weather'][0]['description'], humidity]


    def getWeatherInfo(self):
        return self.weatherInfo

