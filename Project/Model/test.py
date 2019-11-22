from UserData import *
getUser=UserData()
def test():

    print getUser.verify("fenglin","password")
    '''
    print getUser.signUp("fegli1", "password","Feng@gmail.com")
    print getUser.setInformation("Feng", "Lin", "1996-08-06", "Windish")
    '''
    print getUser.vieUserInformation()
    print getUser.setInformation("Feng", "Lin", "1996-08-06", "Windish")
if __name__ == "__main__":
    test()