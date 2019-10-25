class handleException:
    option=1
    userinput=''

    def __init__(self, option, userinput):
        self.option = option
        self.userinput=userinput
        self.inputError

    def inputError(self):
        ## Handle error if user enter city name
        if (self.option == 1):
            if ',' in self.userinput:
                if self.userinput.replace(',', '').replace(' ', '').isalpha():
                    return True
                else:
                    return False
            elif self.userinput.isalpha():
                return True
            else:
                return False
        ## Handle error if user enter zip code
        if (self.option==2):
            if ',' in self.userinput:
                process=self.userinput.replace(' ', '')
                process=process.split(",")
                try:
                    int(process[0])
                except:
                    return False
                if not process[1].isalpha():
                    return False
            else:
                try:
                    int(self.userinput)
                except:
                    return False
            return True
        if (self.option == 3):
            if ',' in self.userinput:
                process = self.userinput.replace(' ', '')
                process = process.split(",")
                try:
                    float(process[0])
                    float(process[1])
                except ValueError:
                    return False
            else:
                return False
            return True




