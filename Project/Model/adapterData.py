class AdapterData:
    interface = None
    def __init__(self, data):
        self.interface = data

    def allData(self):
        return self.interface.allData()
