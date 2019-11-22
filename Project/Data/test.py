from DB import *
getDB=Database()
def test():
    '''
    print(getDB.setUser("fenglin123", "password", "meial@gmail"))
    print(getDB.verifyUser("fenglin123"))
    print(getDB.setUserInfo("1", "Feng", "Lin", "1996-12-18","Windish"))
    '''
    print(getDB.viewUserInfo("1"))
    print(getDB.updateInfo("1", "Feng", "Lin", "1996-07-06", "Wdish"))
    print(getDB.viewUserInfo("1"))


if __name__ == "__main__":
    test()