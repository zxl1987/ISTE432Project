import requests


class APIData:
    input = None
    option = None

    def __init__(self, option, input):
        self.input = input
        self.option = option

    def allData(self):
        if self.option == 1:
            url = 'https://api.openweathermap.org/data/2.5/weather?q=' + self.input + '&appid=a43ce9d89cbceb4d0d7885c7e1476c55'
            data = {'header': 'Content-Type: application/json'}
            r = requests.get(url, data=data)
            data = r.json()
        else:
            data=None
        return data

