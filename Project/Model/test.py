from UserData import *
getUser=UserData()
def test():

    print getUser.verify("fenglin","password")
    '''
    print getUser.signUp("fegli1", "password","Feng@gmail.com")
    print getUser.setInformation("Feng", "Lin", "1996-08-06", "Windish")
    '''
    print getUser.viewUserHistory()
    print getUser.deleteHisiotry("10")
    print getUser.viewUserHistory()
    print getUser.saveHistory(1, "wc")
    print getUser.viewUserHistory()

if __name__ == "__main__":
    test()