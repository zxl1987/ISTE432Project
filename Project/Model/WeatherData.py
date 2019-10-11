from Data.apiData import *
from adapterData import *

class Getdata:
    datainfo = None
    weatherinfo=None
    def __init__(self, data):
        self.datainfo = data

    def processData(self):
        data=self.datainfo.alldata()
        minTemp=(int(data['main']['temp_min'])-273.15) * 9/5+32
        maxTemp=(int(data['main']['temp_max'])-273.15) * 9/5+32
        Temp = (int(data['main']['temp'])-273.15) * 9/5+32
        self.weatherinfo=[round(minTemp, 2), round(maxTemp, 2), round(Temp, 2), data['wind']['speed'], data['weather'][0]['description']]
        self.returnWeather()

    def returnWeather(self):
        return self.weatherinfo


def test():
    cityname = 'Brooklyn'
    getWeather=Weatherdata(1, cityname)
    adapter = Adapter(getWeather)
    printdata  = Getdata(adapter)
    printdata.processData()


if __name__ == "__main__":
    test()