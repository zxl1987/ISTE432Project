import sys
import os
cwd = os.getcwd()
parent_dir = (os.path.abspath(os.path.join(cwd, os.pardir)))
sys.path.append(parent_dir)
from Model.WeatherData import *
from Model.handleException import *

def test():
    cityName = '19, 35'
    option = 3

    handleError = handleException(option, cityName)
    if handleError.inputError():
        printdata = WeatherData(option, cityName)
        print printdata.getWeatherInfo()
    else:
        print "Invalidate input!"


if __name__ == "__main__":
    test()
