import sys
import os
cwd = os.getcwd()
parent_dir = (os.path.abspath(os.path.join(cwd, os.pardir)))
sys.path.append(parent_dir)

from Model.WeatherData import *
from Model.HandleException import *


def test():
    cityName = 'Rochester'
    option = 1

    handleError = HandleException(option, cityName)
    if handleError.inputError():
        printdata = WeatherData(option, cityName)
        print printdata.getWeatherInfo()
    else:
        print "Invalidate input!"


if __name__ == "__main__":
    test()
