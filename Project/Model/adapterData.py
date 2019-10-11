class Adapter():
    interface = None
    def __init__(self, data):
        self.interface = data

    def alldata(self):
        return self.interface.alldata()